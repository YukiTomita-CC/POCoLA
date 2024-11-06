class TaskRanker:
    def rank_tasks(self):
        # <START>
        # due_dateで昇順ソート
        # 同じdue_dateでグループ化して、それぞれimportanceで降順ソート
        # 同じimportanceでグループ化して、それぞれdifficultyで昇順ソート
        
        # 今日のdue_dateだけを取り出す
        # もし要素.estimated_effortの合計が今日のhours_per_dayを超えない場合
            # 今日以外のタスクのリストから最もスコアが高いタスクを取り出す(閾値あり)
                # 今日のタスクのリストに追加して、まだ今日のhours_per_dayを超えない場合はその次のタスクを追加
                    # 一つの段階で超えるようであれば、ユーザーにそのタスクを分割して追加するか、今日のhours_per_dayを増やすか、そもそも追加しないかを選択させる
            # まだ余裕がある場合、今日以外のタスクのリストから最も登録日の古いタスクを取り出す(importanceが低いもの)
                # 今日のタスクのリストに追加して、まだ今日のhours_per_dayを超えない場合はその次のタスクを追加
                    # 以下同様
        # そもそもが今日のhours_per_dayを超える場合
            # まずユーザーに今日のhours_per_dayを増やせるのかを尋ねる
                # できる場合は、今日のhours_per_dayをその分増やして再度タスクを追加する
                # できない場合は、次に行く
            # 今日のタスクのリストの中で、本当に今日までにやらないといけない部分で分割できるものがあるかユーザーに尋ねる
                # できる場合は、そのタスクを分割して今日のhours_per_dayに収まるようにする
                # できない場合は、次に行く
            # 今日のタスクのリストの中で、タスクのdue_dateを後ろ倒しにできるものがあるかユーザーに尋ねる
                # できる場合は、そのタスクを後ろ倒しにして今日のhours_per_dayに収まるようにする
                # できない場合は、次に行く
            # 外部リソースが使えるかユーザーに尋ねる
                # 使える場合は、そのリソースを使う前提で0にして今日のhours_per_dayに収まるようにする
                # 使えない場合は、次に行く
            # マイルストーンのdue_date、もしくはプロジェクトのend_dateが後ろ倒しになる可能性が高いことをユーザーに伝え、次の日に回すタスクを選択させる      
        # プロジェクトでタスクをグループ化して今日のタスクのリストを返す
        # <END>

        # データ作成とかデータアノテーションとか数週間やるやつとかはわざわざ小さいタスクに分割するというよりは、今日は何時間とかにしたいが...。
        # 今日がdue_dateでなくても、estimated_effort大きくて今日手を付けておかないといけないやつとかもある、そういうのはどうするか。
        # 今日が余裕だと思っていても明日due_dateのやつがあって、明日は予定があって時間を割けないとかもある。それは今日やっておかないといけない...。

        raise NotImplementedError()
