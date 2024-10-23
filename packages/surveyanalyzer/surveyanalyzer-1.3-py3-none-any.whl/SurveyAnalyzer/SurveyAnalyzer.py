import json
import re
import jaconv #半角→全角用
import queue
import os, time
from threading import Thread
from collections import Counter

# import myopenai
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List

# クラスタリング用
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer #TF-IDF用
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform

#wordcloud用
import MeCab
from collections import Counter
from wordcloud import WordCloud


class SurveyAnalyzer :
    fld_workdata    = None
    l_text          = []
    d_vector        = {} #手法ごと(embedding/tfidf)に分かれてる（中身はリスト）
    d_cluster       = {}
    dic_cluster_info  = {}
    queue_progress  = None
    mo              = None
    client          = None #embeddingで使用

    class openai_so :
        client = None
        prompts_for_so = []
        model = None
        model_emb = None

        def __init__(self, model:str, model_emb:str) :
            load_dotenv()
            self.client = OpenAI()
            self.model = model
            self.model_emb = model_emb

        def create_message_so(self, role, prompt) :
            self.prompts_for_so.append({"role":role, "content":prompt})
        def delete_all_message(self) :
            self.prompts_for_so = []
        def run_so(self, ResponseStep) :
            try:
                response = self.client.beta.chat.completions.parse(
                    model           = self.model,
                    temperature     = 0,
                    messages        = self.prompts_for_so,
                    response_format = ResponseStep,
                )
                return response.choices[0].message.parsed
            except Exception as e:
                print(f"エラー：{e}")
                return None
        def embeddings(self, txt, model_:str=None) :
            model = model_ if model_ else self.model_emb
            response = self.client.embeddings.create(input=txt, model=model)
            return response.data[0].embedding
        



    
    def __init__(self, fld_workdata:str) :
        if not os.path.exists(fld_workdata) :
            os.mkdir(fld_workdata)
        self.fld_workdata   = fld_workdata
        self.queue_progress = queue.Queue()

    def init_openai(self, gptmodel:str, embmodel:str="text-embedding-3-small") :
        self.mo = self.openai_so(gptmodel, embmodel)

    def set_textdata(self, l_text:list) :
        self.l_text = l_text

    def get_text(self, clustertype:str=None, clusterno:int=None) :
        if not clustertype :
            return self.l_text
        
        l_target = []
        for i, v in enumerate(sa.d_cluster[clustertype]) :
            if v == clusterno :
                l_target.append(sa.l_text[i])
        return l_target
    
    #---------------------------------------------------#
    #--- ベクトル化 -------------------------------------#
    #---------------------------------------------------#
    #embedding
    def calculate_vector_embedding(self, model_emb:str=None) :
        l_vector = []
        n_max = len(self.l_text)
        for txt in self.l_text :
            self.queue_progress.put(f'ベクトル処理（Embedding: {len(l_vector)+1}/{n_max}）...')
            response = self.mo.embeddings(txt, model_emb)
            l_vector.append( response )

        self.d_vector["embedding"] = l_vector
        self.queue_progress.put('done')

    # TF-IDF
    def calculate_vector_tfidf(self, l_parts:list=["名詞", "動詞", "形容詞"]) :
        # 形態素解析を行う関数を定義する
        def tokenize(text):
            mecab = MeCab.Tagger('-Ochasen')
            mecab.parse('')
            node = mecab.parseToNode(text)
            words = []
            while node:
                # 名詞、動詞、形容詞だけを抽出
                if node.feature.split(",")[0] in l_parts:
                    words.append(node.surface)
                node = node.next
            return words

        # 'text'列に対して形態素解析を行う
        l_tokenized_text = []
        for txt in self.l_text :
            l_tokenized_text.append( " ".join(tokenize(txt)) )

        # TF-IDFでベクトル化する
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(l_tokenized_text)

        # ベクトルをリスト型に変換
        self.d_vector["tfidf"] = X.toarray().tolist()

    #---------------------------------------------------#
    #--- クラスター処理 ---------------------------------#
    #---------------------------------------------------#
    #最適なクラスタサイズを計算
    def optimize_cluster_size(self, vector_type:str, n_cluster_min:int=3, n_cluster_max:int=9, f_showchart:bool=False, f_savechart:bool=False) -> int :
        #vector_type : tfidf / embedding
        l_vector = self.d_vector[vector_type]
        X = l_vector
        range_n_clusters = range(n_cluster_min, n_cluster_max+1)  # クラスタ数を2から9まで試す
        silhouette_scores = []

        for n_clusters in range_n_clusters:
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            kmeans.fit(X)
            silhouette_scores.append( silhouette_score(X, kmeans.labels_) )


        # シルエットスコアの結果をプロット
        plt.ioff()
        plt.figure(figsize=(10, 5))
        plt.plot(range_n_clusters, silhouette_scores, marker='o')
        plt.xlabel('Number of clusters')
        plt.ylabel('Silhouette Score')
        plt.title('Silhouette Analysis for Optimal Number of Clusters')
        if f_showchart :
            plt.show()
        if f_savechart :
            file_path =os.path.join(self.fld_workdata, "optimal_clustersize.png")
            if os.path.exists(file_path) :
                os.remove(file_path)
            plt.savefig(file_path) 

        # 最適なクラスタ数を決定（例：シルエットスコアが最大のクラスタ数）
        optimal_clustersize = range_n_clusters[np.argmax(silhouette_scores)]
        return optimal_clustersize

    #クラスタリング
    def clustering(self, vector_type:str, n_cluster:int) -> list :
        #vector_type : tfidf / embedding
        l_vector = self.d_vector[vector_type]

        kmeans = KMeans(n_clusters=n_cluster) #, random_state=42)
        kmeans.fit(l_vector)
        l_cluster = [int(x+1) for x in kmeans.labels_]

        self.d_cluster[vector_type] = l_cluster
        return l_cluster


    #--- Embeddingのクラスタとtfidfのクラスタを統合 ----------------#
    def clustering_emb_x_tfidf(self) :
        # Assume l_text, l_cluster_by_embedding, and l_cluster_by_tfidf are provided
        N = len(self.l_text)
        l_cluster_by_embedding = self.d_cluster["embedding"]
        l_cluster_by_tfidf     = self.d_cluster["tfidf"]
        
        # Initialize the co-association matrix
        co_assoc = np.zeros((N, N))

        # Compute the co-association matrix
        for i in range(N):
            for j in range(i, N):
                count = 0
                if l_cluster_by_embedding[i] == l_cluster_by_embedding[j]:
                    count += 1
                if l_cluster_by_tfidf[i] == l_cluster_by_tfidf[j]:
                    count += 1
                co_assoc[i][j] = count
                co_assoc[j][i] = count  # Ensure symmetry

        # Convert co-association matrix to a distance matrix
        distance_matrix = 2 - co_assoc  # Maximum co-association is 2
        condensed_distance = squareform(distance_matrix)

        # Perform hierarchical clustering
        Z = linkage(condensed_distance, method='average')

        # Determine the optimal number of clusters
        num_clusters_embedding = len(set(l_cluster_by_embedding))
        num_clusters_tfidf = len(set(l_cluster_by_tfidf))
        num_clusters = (num_clusters_embedding + num_clusters_tfidf) // 2

        # Assign cluster labels
        cluster_labels_list = fcluster(Z, num_clusters, criterion='maxclust').tolist()
        # Output the final cluster assignments
        # for text, cluster_label in zip(self.l_text, cluster_labels_list):
        #     print(f"Text: {text}, Cluster: {cluster_label}")
        self.d_cluster["comb_ext"] = cluster_labels_list

    #---------------------------------------------#
    #クラスターのタイトル付け 
    #---------------------------------------------#
    def generate_cluster_title(self, vector_type:str, model_:str=None, n_max_charactors:int=10000) :
        #n_max_charactors: 生成AIに投げる際の最大文字数
        #vector_type : tfidf / embedding / comb_ext
        l_cluster = self.d_cluster[vector_type]
        #クラスターごとにコメントを振り分け
        max_cluster = int( max(l_cluster) )
        dic_comments = {}
        for cluster_no in range(1, max_cluster+1) :
            dic_comments[cluster_no] = []

        for i in range(len(self.l_text)) :
            cluster_no = l_cluster[i]
            dic_comments[cluster_no].append( self.l_text[i] )

        #プロンプトづくり
        comment = ""
        l_comments = []
        for cluster_no in range(1, max_cluster+1) :
            temp_comment  = f"#Cluster No:{cluster_no}\n"
            temp_comment += '\n'.join('- ' + text.strip() for text in dic_comments[cluster_no])
            temp_comment += "\n"
            if len(comment) + len(temp_comment) <= n_max_charactors :
                comment += temp_comment
            else :
                l_comments.append(comment)
                comment = temp_comment
        l_comments.append(comment)

        #GPT照会
        class ClusterInfo(BaseModel):
            ClusterNo       :   str
            ClusterTitle    : str       = Field(...,description="このクラスターのタイトル")
            TipicalText     : List[str] = Field(...,description="代表的な文章（５つ）")
        class ClusterInfoList(BaseModel):
            l_clusterinfo   :   List[ClusterInfo]

        dic2 = {}
        for idx, comment in enumerate(l_comments) :
            prompt = f'''
                文章群に対してクラスタリングを行い分類した。それぞれのクラスターに付けるタイトルを、そこに属している文章を元に考えてほしい。
                また、そのクラスターの代表的な文章を5つ選出してください。

                文章群: """
                {comment}
                """
            '''
            prompt = prompt.replace("                ", "").strip()

            self.mo.delete_all_message()
            self.mo.create_message_so("user", prompt)
            self.queue_progress.put(f'タイトル生成: {idx+1}/{len(l_comments)} ...')
            response = self.mo.run_so(ClusterInfoList)
            l_clusterinfo = [ x.model_dump() for x in response.l_clusterinfo ]

            #清書
            for x in l_clusterinfo :
                dic2[x['ClusterNo']] = {'title': x["ClusterTitle"], '代表的な文章': x["TipicalText"]}

        self.queue_progress.put(f'done')
        self.dic_cluster_info[vector_type] = dic2
        return self.dic_cluster_info

    #---------------------------------------------#
    # ユーザー指定のクラスタ操作 
    #---------------------------------------------#
    #--- ユーザー指定クラスタをセット ---------------#
    def set_user_categories(self, l_clustername:list) :
        lll = l_clustername.copy()
        if 'その他' not in lll :
            lll.append('その他')

        dic = {}
        for idx in range(len(lll)) :
            dic[idx+1] = {'title': lll[idx]}
        self.dic_cluster_info["user"] = dic

    #--- ユーザー指定クラスタでクラスタリング ---------------#
    def clustering_with_user_categories(self, l_clustername_:list=None, step=1000) :
        #step: リストが大きい時にパンクするので、step個ずつに区切って処理する
        if l_clustername_ :
            self.set_user_categories(l_clustername_)
        self.dic_cluster_info['user'] = {k: self.dic_cluster_info['user'][k] for k in sorted(self.dic_cluster_info['user'], key=lambda x: int(x))}
        txt_cluster = '\n'.join( [ f"{k},{v['title']}" for k,v in self.dic_cluster_info['user'].items() ] )

        class text_cluster(BaseModel):
            text_no         :   int
            Cluster_No      :   int
        class text_clusters(BaseModel):
            l_cluster       :   List[text_cluster]

        prompt_base = '''
            以下の文章を分類したい。それぞれの文章がどの分類Noに該当するかを分析してください。

            # 分類: """
            Cluster_No, 分類名
            {cluster}
            """

            # 文章: """
            text_no, 文章
            {text}
            """
        '''.replace("            ","").strip()

        l_text_local = [ f"{i}, {text}" for i, text in enumerate(self.l_text  ) ]
        l_text_cluster = []
        step = 1000
        for i in range(0, len(l_text_local), step) :
            txt_text = '\n'.join( l_text_local[i:i+step] )
            prompt = prompt_base.format(cluster=txt_cluster, text=txt_text)

            self.mo.delete_all_message()
            self.mo.create_message_so("user", prompt)
            response = self.mo.run_so(text_clusters)
            l_text_cluster.extend( [ x.model_dump() for x in response.l_cluster ] )
        
        result_list = [None] * (max([x['text_no'] for x in l_text_cluster]) + 1)
        for x in l_text_cluster:
            result_list[x['text_no']] = x['Cluster_No']
        self.d_cluster["user"] = result_list
        count = Counter(result_list)
        count = dict(sorted(count.items()))
        print(count)

    #--- その他に該当した文章から新たに分類名を新設 ---------------#
    def bunseki_sonota(self) :
        sonota_id = int( [ k for k,v in self.dic_cluster_info['user'].items() if v['title'] == 'その他' ][0] )
        txt_text = ""
        for i, x in enumerate(self.d_cluster['user']) :
            if x == sonota_id :
                txt_text += f"{i}, {self.l_text[i]}\n"

        txt_bunrui = ','.join( [ x["title"] for x in self.dic_cluster_info['user'].values() ] )
        prompt_base = '''
            以下の文章を分類分けしたが、「その他」に分類されたものをより詳細に分析して、分類名を新設したい。
            現在は `[{curr_bunrui}]` という分類名だが、ここに追加すべき新たな分類名を考えてください。

            # "その他"に分類された文章: """
            text_no, 文章
            {text}
            """
        '''.replace("            ","").strip()

        class new_cluster_name(BaseModel):
            l_new_cluster_name  :   List[str]

        prompt = prompt_base.format(curr_bunrui=txt_bunrui, text=txt_text)
        self.mo.delete_all_message()
        self.mo.create_message_so("user", prompt)
        response = self.mo.run_so(new_cluster_name)

        for i, x in enumerate(response.l_new_cluster_name) :
            self.dic_cluster_info['user'][str(sonota_id+i)] = {'title':f"{x}(*)"}
        self.dic_cluster_info['user'][str(sonota_id+len(response.l_new_cluster_name))] = {'title':'その他'}
        
    #---------------------------------------------------------#
    # そのクラスターの代表的な質問を生成
    #---------------------------------------------------------#
    def generate_representative_inquires(self, l_targettext:list, n_inquires:int=3) :
        class Response_Inquires(BaseModel) :
            index       : int = Field(...,description="多さの順番（1が最も多い質問、2が次に多い質問、、、")
            inquire     : str = Field(...,description="代表的な質問")
            explanation : str = Field(...,description="解説や特記事項")
        class Response_so(BaseModel) :
            l_inquires  : List[Response_Inquires]

        prompt_base = '''
        以下の問い合わせ履歴を分析して、代表的な問い合わせ事例を多い順から{n_inquires}個教えてください。
        
        問い合わせ履歴: """
        {rireki}
        """
        '''.replace("        ", "")

        rireki = '\n'.join(l_targettext)
        prompt = prompt_base.format(n_inquires=n_inquires, rireki=rireki)
        self.mo.delete_all_message()
        self.mo.create_message_so("user", prompt)
        response = self.mo.run_so(Response_so)
        l_inquires = [ x.model_dump() for x in response.l_inquires ]

        return l_inquires







    #---------------------------------------------------------#
    #--- Word Cloud ------------------------------------------#
    #---------------------------------------------------------#
    def generate_wordcloud(self, fn:str, fld:str=None) :
        if not fld :
            fld = self.fld_workdata

        exclude_words = ['こと']
        self.__myworcloud(self.l_text, exclude_words, fn, fld_save=fld)

    def __myworcloud(self, l_txt:list, l_exclude_words:list, fn:str, fld_save:str, font_path:str='C:/Windows/Fonts/meiryo.ttc', userdic:str=None) :
        # MeCabのTaggerを初期化
        if userdic :
            mecab = MeCab.Tagger(f'-u {userdic}')
        else :
            mecab = MeCab.Tagger()

        # 単語カウンターの初期化
        word_counter = Counter()

        # Q2列のフリーコメントを形態素解析
        for comment in l_txt:
            parsed = mecab.parse(comment)
            parsed_lines = parsed.split('\n')
            for line in parsed_lines:
                if line == 'EOS' or line == '':
                    continue
                word_info = line.split('\t')
                if len(word_info) > 1:
                    word = word_info[0]
                    # 品詞情報を取得
                    details = word_info[1].split(',')
                    # 名詞のみをカウント
                    if details[0] == '名詞':
                        word_counter[word] += 1

        # 除外単語をカウンターから削除
        for word in l_exclude_words:
            if word in word_counter:
                del word_counter[word]

        # 頻出単語のカウント結果を辞書に変換
        word_freq = dict(word_counter)

        # ワードクラウドの生成
        wordcloud = WordCloud(font_path=font_path, background_color='white', width=800, height=600).generate_from_frequencies(word_freq)
        if not os.path.exists(fld_save):
            os.makedirs(fld_save)
        wordcloud.to_file(f"{fld_save}/{fn}")

    #------------------------------------------------------------------#
    #--- 便利関数 ------------------------------------------------------#
    #------------------------------------------------------------------#
    #--- 読点もしくは改行で文章を区切る -----------------#
    def split_by_delimiter(self, l_text_:list=None) -> list :
        l_text2 = []
        if l_text_ is None :
            l_text = self.l_text
        else :
            l_text = l_text_.copy()

        for txt in l_text :
            split_parts = re.split(r'。|\n', txt)
            for part in split_parts:
                if part.strip():  # 空文字列を無視
                    l_text2.append(part.strip() + "。")  # 「。」を追加して整形

        if l_text_ is None :
            self.l_text = l_text2

        return l_text2

    #--- 全角に変換 -----------------------------------#
    def han_to_zen(self, l_text_:list=None) -> list :
        l_res = []
        l_text = l_text_
        if l_text_ is None :
            l_text = self.l_text
        for txt in l_text :
            l_res.append( jaconv.h2z(txt, ascii=True, digit=True) )
        if l_text_ is None :
            self.l_text = l_res
        return l_res

    #--- 固有名詞を●●（人名は▲▲）に変換する -------------#
    def koyuu_meishi_killer(self, l_text_:list=None, userdic:str=None) -> list:
        l_text = l_text_
        if l_text_ is None :
            l_text = self.l_text

        if userdic :
            mecab = MeCab.Tagger(f'-Ochasen -u {userdic}')
        else :
            mecab = MeCab.Tagger('-Ochasen')

        def __koyuu_meishi_killer(txt:str) :
            node = mecab.parseToNode(txt)
            result = []
            while node:
                # 品詞情報の取得
                features = node.feature.split(',')
                if features[0] == '名詞' and features[1] == '固有名詞':
                    if features[2] == '人名':
                        result.append('▲▲') # 人名の場合は「▲▲」に置換
                    else:
                        result.append('●●')
                else:
                    # 固有名詞でない場合はそのまま
                    result.append(node.surface)
                node = node.next
            return ''.join(result)

        l_res = []
        for txt in l_text :
            l_res.append( __koyuu_meishi_killer(txt) )

        if l_text_ is None :
            self.l_text = l_res

        return l_res

    #--- JSON抽出 ----------------------------------------#
    def __myjson(self, txt:str)->dict :
        pattern = r'```json(.*?)```'
        match = re.search(pattern, txt, re.DOTALL)
        dic = {}
        if match:
            json_str = match.group(1).strip()
            try:
                dic = json.loads(json_str)
            except json.JSONDecodeError as e:
                print(f'JSONデコードエラー: {e}')
        else:
            print('マッチするパターンが見つかりませんでした。')

        return dic

    #--- クラスタごとのカウント ----------------------------#
    def count_by_cluster(self, ctype) :
        d = self.d_cluster[ctype]
        count = Counter(d)
        count = dict(sorted(count.items()))
        res = {}
        for k,v in count.items() :
            cname = self.dic_cluster_info[ctype][str(k)]["title"]
            res[cname] = v
        return res


    #--- Save ------------------------------------------------#
    def savedata(self, fn:str="sa_data.json", f_include_vectordata:bool=True) :
        # f_include_vectordata: Falseだとベクターデータは保存しない（でかいから時間がかかる）
        dic = {}
        dic['l_text'        ] = self.l_text
        if f_include_vectordata :
            dic['d_vector'      ] = self.d_vector
        dic['d_cluster'     ] = self.d_cluster
        dic['dic_cluster_info'] = self.dic_cluster_info

        file_path = os.path.join( self.fld_workdata, fn )
        with open(file_path, "w", encoding='utf-8') as f:
            json.dump(dic, f, ensure_ascii=False, indent=4)

    #ベクターデータだけを保存（でかいから、保存したいタイミングだけで保存できるように）
    def save_vectordata(self, fn:str="sa_data_vector.json") :
        file_path = os.path.join( self.fld_workdata, fn )
        with open(file_path, "w", encoding='utf-8') as f:
            json.dump(self.d_vector, f, ensure_ascii=False, indent=4)

    #--- Load ------------------------------------------------#
    def loaddata(self, fn:str="sa_data.json") :
        file_path = os.path.join( self.fld_workdata, fn )
        with open(file_path, "r", encoding='utf-8') as f:
            dic = json.load(f)

        self.l_text         = dic['l_text'        ]
        if "d_vector" in dic.keys() :
            self.d_vector       = dic['d_vector'      ]
        self.d_cluster      = dic['d_cluster'     ]
        self.dic_cluster_info = dic['dic_cluster_info']

    def load_vectordata(self, fn:str="sa_data_vector.json") :
        file_path = os.path.join( self.fld_workdata, fn )
        with open(file_path, "r", encoding='utf-8') as f:
            self.d_vector = json.load(f)



if __name__ == "__main__" :

    #初期化
    model       = 'gpt-4o-2024-08-06'
    model_emb   = 'text-embedding-3-small'
    sa          = SurveyAnalyzer("data")
    sa.init_openai(model, model_emb)
    l_vector_type = ["embedding", "tfidf"]

    #サンプルデータ読み込み
    with open("SurveyAnalyzer/samplecommentdata.txt", "r", encoding="utf-8") as f:
        txt = f.read()
    l_text = txt.split('\n')
    l_text = [x for x in l_text if x.strip()]

    #データセット
    sa.set_textdata(l_text)

    #ワードクラウド
    sa.generate_wordcloud("wordcloud.png")
    #半角→全角
    sa.han_to_zen()
    #改行や読点(。)で区切る
    sa.split_by_delimiter()
    #固有名詞つぶし
    sa.koyuu_meishi_killer()

    for vector_type in l_vector_type :
        if vector_type == "tfidf" :
            #ベクトル化（TF-IDF）
            sa.calculate_vector_tfidf(l_parts=["名詞","動詞"])
        elif vector_type == "embedding" :
            # #ベクトル化（エンベディング）
            # sa.calculate_vector_embedding()
            #ベクトル化（エンベディング）--- 別スレッドでの実行例
            thread = Thread(target=sa.calculate_vector_embedding, args=())
            thread.start()
            while True:
                message = sa.queue_progress.get()
                print(message)
                if message == 'done':
                    break
                else:
                    pass

        #クラスタ数の計算
        optimal_cluster_size = sa.optimize_cluster_size(vector_type=vector_type, n_cluster_min=3, n_cluster_max=9, f_showchart=False, f_savechart=True)
        #クラスタリング
        sa.clustering(vector_type=vector_type, n_cluster=optimal_cluster_size)

    #いったん保存
    sa.savedata()

    #保存データの読み込み
    sa.loaddata()

    # Embeddingのクラスタとtfidfのクラスタを掛け合わせ
    sa.clustering_emb_x_tfidf()

    #クラスター情報生成（クラスター名をつける＆代表コメント抽出）
    thread = Thread(target=sa.generate_cluster_title,  kwargs={"vector_type": "comb_ext", "n_max_charactors": 500} )
    thread.start()
    while True:
        message = sa.queue_progress.get()
        print(message)
        if message == 'done':
            break
        else:
            pass

    #保存
    sa.savedata()

    #保存データの読み込み
    sa.loaddata()
    l_usercluster = ['研修時間', '実践的', '分かりやすさ', '改善の余地', '理論的']
    sa.clustering_with_user_categories(l_usercluster)
    sa.savedata()

    sa.loaddata()
    sa.bunseki_sonota()
    sa.savedata()
    sa.loaddata()
    sa.clustering_with_user_categories()
    sa.savedata()

    sa.loaddata()
    res = sa.count_by_cluster("user")
    print(res)

