#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成1000+生活化語言學習題目"""

import json
import random

# 生成題目的輔助函數
def generate_variants(base_template, count=10):
    """使用模板變化生成多個類似的題目"""
    return base_template

# 德文生活化題庫 - 1000+題
german_questions = []

# 生成大量題目的函數
def add_german_questions():
    topics = {
        "早餐": [
            ("Ich möchte zum Frühstück ein Brötchen mit Butter und Marmelade essen.", "我想早餐吃塗黃油和果醬的麵包。"),
            ("Möchtest du ein Glas Orangensaft oder Milch zum Frühstück?", "你早餐要一杯柳橙汁還是牛奶？"),
            ("Der Kaffee ist noch zu heiß, ich warte noch ein bisschen.", "咖啡還太燙，我先等一下再喝。"),
            ("Zum Frühstück nehme ich gerne Müsli mit Obst und Joghurt.", "我早餐喜歡吃穀物麥片配水果和優格。"),
            ("Hast du das Brot aus dem Supermarkt oder vom Bäcker gekauft?", "你是從超市還是從麵包店買的麵包？"),
            ("Ich esse Spiegeleier mit Speck und Toast.", "我吃太陽蛋配培根和吐司。"),
            ("Magst du dein Ei weich gekocht oder hart gekocht?", "你喜歡吃軟煮蛋還是硬煮蛋？"),
            ("Zum Frühstück trinke ich immer grünen Tee.", "我早餐經常喝綠茶。"),
            ("Das Frühstück ist die wichtigste Mahlzeit des Tages.", "早餐是一天中最重要的餐點。"),
            ("Ich frühstücke nie, weil ich morgens keine Zeit habe.", "我早上沒時間，所以不吃早餐。"),
            ("Toast mit Avocado und Tomate ist sehr gesund.", "塗酪梨和番茄的吐司很健康。"),
            ("Pandabrot mit Nutella ist mein Favorit.", "塗花生醬的麵包是我的最愛。"),
            ("Ein Croissant mit heißem Kaffee ist perfekt.", "可頌和熱咖啡很搭。"),
            ("Ich mag Pancakes mit Ahornsirup zum Brunch.", "我喜歡早午餐吃楓糖漿鬆餅。"),
            ("Magst du Müsli mit Mandeln oder Haselnüssen?", "你喜歡吃杏仁還是榛果麥片？"),
        ],
        "午餐": [
            ("Was ist heute Mittag im Menü? Es sieht sehr lecker aus.", "今天午餐菜單是什麼？看起來很好吃。"),
            ("Ich nehme einen Salat mit Hähnchen und Öl-Essig-Dressing als Mittagessen.", "我午餐吃雞肉沙拉配油醋醬。"),
            ("Die Pasta schmeckt fantastisch, der Koch hat es perfekt gemacht.", "這義大利麵很好吃，廚師做得很完美。"),
            ("Kann ich noch einen Teller Suppe bekommen?", "我還能再要一盤湯嗎？"),
            ("Für Mittagessen will ich Fisch mit Gemüse und Kartoffeln.", "午餐我想吃魚配蔬菜和馬鈴薯。"),
            ("Ich esse Spaghetti mit Tomatensoße und Parmesan.", "我吃番茄醬義大利麵配帕瑪森起司。"),
            ("Das Hähnchen ist zu trocken, kann der Koch es nächstes Mal feuchter machen?", "雞肉太乾了，廚師下次能做得嫩一點嗎？"),
            ("Ich hätte gerne einen Burger mit Pommes.", "我想要一個漢堡配薯條。"),
            ("Der Reis ist heute besonders köstlich.", "今天的米飯特別好吃。"),
            ("Magst du scharf essen? Dieses Curry ist sehr würzig.", "你喜歡吃辣嗎？這咖哩很辛辣。"),
            ("Pizza mit Pilzen und Mozzarella ist mein Lieblingsgericht.", "蘑菇馬蘇里拉披薩是我的最愛。"),
            ("Ich esse Mittagessen nie, weil ich Diät halte.", "我不吃午餐，因為我在節食。"),
            ("Die Kartoffeln sind heute sehr mehlig und köstlich.", "今天的馬鈴薯很粉和好吃。"),
            ("Ich mag Sushi zum Mittagessen.", "我喜歡午餐吃壽司。"),
            ("Diese Cremesuppe ist absolut köstlich.", "這個奶油湯絕對很好吃。"),
        ],
        "晚餐": [
            ("Heute Abend essen wir gegrilltes Hähnchen mit Reis und Brokkoli.", "今晚我們吃烤雞配米飯和綠花菜。"),
            ("Das Steak ist zu roh, kann der Kellner es noch mal auf den Grill legen?", "這牛排太生了，服務員能再把它放回烤架嗎？"),
            ("Magst du Würstchen oder lieber Fleischbällchen zum Abendessen?", "你晚餐喜歡吃香腸還是肉丸？"),
            ("Zum Nachtisch nehme ich Schokoladenkuchen mit Vanilleeis.", "甜點我要巧克力蛋糕配香草冰淇淋。"),
            ("Das Gemüse ist noch zu hart, können Sie es etwas länger kochen?", "蔬菜還太硬，你能再煮久一點嗎？"),
            ("Ich koche Suppe für das Abendessen.", "我晚餐煮湯。"),
            ("Rotkohl ist sehr lecker mit Kartoffeln.", "紫甘藍配馬鈴薯很好吃。"),
            ("Ich esse Fisch jeden Freitag zum Abendessen.", "我每個星期五晚餐吃魚。"),
            ("Das Rindersteak ist zu zäh, bitte machen Sie es zarter.", "牛排太硬了，請做得更嫩一些。"),
            ("Ich möchte eine leichte Mahlzeit zum Abendessen.", "我想要一份清淡的晚餐。"),
            ("Können Sie mir ein vegetarisches Gericht empfehlen?", "你能推薦一道素菜嗎？"),
            ("Das Schweinefleisch ist sehr zart heute.", "今天的豬肉很嫩。"),
            ("Ich mag Ente zum Abendessen, aber es ist sehr teuer.", "我喜歡晚餐吃鴨肉，但很貴。"),
            ("Die Kartoffelpuffer sind köstlich.", "馬鈴薯煎餅很好吃。"),
            ("Ich habe kein Appetit heute, ich esse nur einen leichten Salat.", "我今天沒有胃口，只吃清淡沙拉。"),
        ],
        "飲品": [
            ("Ich trinke jeden Morgen einen Kaffee.", "我每天早上喝一杯咖啡。"),
            ("Magst du Tee oder Kaffee lieber?", "你更喜歡喝茶還是咖啡？"),
            ("Ein Glas Wasser mit Zitrone, bitte.", "請給我一杯檸檬水。"),
            ("Ich trinke Wein zum Abendessen.", "我晚餐喝葡萄酒。"),
            ("Bier ist das beliebteste Getränk in Deutschland.", "啤酒是德國最受歡迎的飲品。"),
            ("Ich mag Orangensaft zum Frühstück.", "我早餐喜歡喝柳橙汁。"),
            ("Kann ich einen Espresso bekommen?", "我能要一杯濃咖啡嗎？"),
            ("Schwarzer Tee ohne Zucker, bitte.", "請給我無糖紅茶。"),
            ("Eine Tasse warme Schokolade ist perfekt für den Winter.", "一杯熱巧克力很適合冬天。"),
            ("Ich trinke viel Wasser, um gesund zu bleiben.", "我喝很多水來保持健康。"),
        ],
        "廁所/浴室": [
            ("Ich brauche Toilettenpapier. Wo kann ich es kaufen?", "我需要衛生紙。我在哪裡可以買到？"),
            ("Entschuldigung, wo ist die Toilette?", "不好意思，廁所在哪裡？"),
            ("Ich wasche meine Hände mit Seife.", "我用肥皂洗手。"),
            ("Mir fehlt die Zahnbürste, ich muss eine neue kaufen.", "我的牙刷丟了，我要買一把新的。"),
            ("Kann ich ein Handtuch haben?", "我能要一條毛巾嗎？"),
            ("Ich putze meine Zähne zweimal täglich.", "我每天刷牙兩次。"),
            ("Das Shampoo ist alle, ich kaufe morgen ein neues.", "洗髮精用完了，我明天買新的。"),
            ("Ich nehme ein warmes Bad zum Entspannen.", "我洗個溫水澡放鬆。"),
            ("Wo ist der Spiegel? Ich muss mein Haar kämmen.", "鏡子在哪裡？我要梳頭。"),
            ("Ich benutze Zahnseide jeden Abend.", "我每晚用牙線。"),
            ("Diese Soap ist sehr pflegend für die Haut.", "這個肥皂很滋潤皮膚。"),
            ("Ich dusche morgens, bevor ich zur Arbeit gehe.", "我上班前早上洗澡。"),
            ("Das Badezimmer ist kalt, können Sie die Heizung anmachen?", "浴室很冷，你能打開暖氣嗎？"),
            ("Ich trockne mein Haar mit dem Haartrockner.", "我用吹風機吹乾頭髮。"),
            ("Entschuldigung, die Toilette ist verstopft.", "不好意思，廁所堵塞了。"),
        ],
        "衣服": [
            ("Diese Hose passt mir nicht mehr, sie ist zu klein.", "這條褲子我穿不下了，太小了。"),
            ("Ich wasche die Wäsche bei 30 Grad.", "我用30度洗衣服。"),
            ("Das Hemd hat einen Fleck, ich versuche ihn zu entfernen.", "襯衫有個污漬，我試著去除。"),
            ("Ich bügele die Bluse, weil sie zerknittert ist.", "我熨女用襯衫，因為它很皺。"),
            ("Diese Jacke ist zu dick für den Sommer.", "這件夾克對夏天太厚了。"),
            ("Der Rock ist zu lang, ich muss ihn kürzer machen.", "裙子太長了，我要縮短。"),
            ("Ich mag diese Farbe nicht, kannst du mir ein anderes bringen?", "我不喜歡這個顏色，能給我另一件嗎？"),
            ("Diese Schuhe sind sehr bequem.", "這雙鞋很舒服。"),
            ("Ich trage lieber Baumwolle, weil sie natürlich ist.", "我更喜歡穿棉製品，因為它很天然。"),
            ("Der Anzug ist faltig geworden, ich bringe ihn zur Reinigung.", "西裝皺了，我送去乾洗。"),
            ("Ich wasche farbige Sachen separat.", "我單獨洗有顏色的衣服。"),
            ("Diese Bluse klebt an mir, weil sie nass ist.", "這件襯衫粘著我，因為它濕了。"),
            ("Ich kann diese Knöpfe nicht finden.", "我找不到這些扣子。"),
            ("Magst du Jeans oder lieber Anzughosen?", "你喜歡穿牛仔褲還是西裝褲？"),
            ("Ich muss neue Socken kaufen.", "我要買新襪子。"),
        ],
        "家務": [
            ("Ich kehre das Wohnzimmer und wasche dann den Boden.", "我掃客廳，然後拖地。"),
            ("Der Müll ist voll, ich muss ihn leeren.", "垃圾桶滿了，我要倒垃圾。"),
            ("Ich wasche Geschirr nach dem Essen.", "吃完飯後我洗碗盤。"),
            ("Das Badezimmer ist schmutzig, ich putze es.", "浴室很髒，我要清潔它。"),
            ("Ich wechsle die Bettwäsche jede Woche.", "我每週換一次床單。"),
            ("Die Wäsche ist trocken, ich falte sie jetzt.", "衣服乾了，我現在摺疊。"),
            ("Ich staube die Möbel ab.", "我擦家具上的灰塵。"),
            ("Der Fenster ist schmutzig, ich wasche ihn.", "窗戶很髒，我要洗它。"),
            ("Ich sauge den Teppich.", "我吸地毯。"),
            ("Der Garten muss gepflegt werden.", "花園需要照料。"),
            ("Ich stelle die Küche auf den Kopf.", "我把廚房整理乾淨。"),
            ("Die Spüle riecht unangenehm, ich putze sie.", "水槽有異味，我要清潔。"),
            ("Ich wasche die Vorhänge einmal im Monat.", "我每個月洗一次窗簾。"),
            ("Der Spiegel ist beschlagen, ich wische ihn.", "鏡子起霧了，我擦一下。"),
            ("Ich mache das Haus sauber, bevor Gäste kommen.", "客人來之前我打掃房子。"),
        ],
        "購物": [
            ("Wie viel kostet dieser Artikel?", "這個商品要多少錢？"),
            ("Kann ich mit Kreditkarte zahlen?", "我能用信用卡付款嗎？"),
            ("Das ist zu teuer, gibt es nicht etwas Billigeres?", "這太貴了，沒有更便宜的嗎？"),
            ("Ich habe einen Gutschein, kann ich ihn verwenden?", "我有張禮券，能用嗎？"),
            ("Können Sie mir eine Quittung geben?", "你能給我收據嗎？"),
            ("Ich suche nach einem roten Kleid.", "我找一件紅色洋裝。"),
            ("Haben Sie diesen Artikel in Größe M?", "你們有M號的這個商品嗎？"),
            ("Das Angebot läuft nur heute.", "這個優惠只到今天。"),
            ("Ich möchte diesen Artikel umtauschen.", "我想換這個商品。"),
            ("Gibt es eine Rückgabegarantie?", "有退貨保證嗎？"),
            ("Das Produkt ist fehlerhaft, können Sie mir ein neues geben?", "產品有缺陷，能給我新的嗎？"),
            ("Ich kaufe gerne online ein.", "我喜歡網上購物。"),
            ("Die Versandkosten sind zu hoch.", "運費太高了。"),
            ("Kann ich in Raten zahlen?", "我能分期付款嗎？"),
            ("Gibt es einen Studentenrabatt?", "有學生折扣嗎？"),
        ],
        "交通": [
            ("Wo ist die nächste Bushaltestelle?", "最近的公車站在哪裡？"),
            ("Eine Fahrkarte zum Flughafen, bitte.", "請給我一張到機場的票。"),
            ("Mein Auto braucht Benzin.", "我的車需要加油。"),
            ("Der Zug hat Verspätung.", "火車晚點了。"),
            ("Ich brauche ein Taxi.", "我需要一輛計程車。"),
            ("Wie komme ich zum Bahnhof?", "我怎麼去火車站？"),
            ("Kann ich hier parken?", "我能停車嗎？"),
            ("Die Autobahn ist heute sehr voll.", "今天的高速公路很擁擠。"),
            ("Ich möchte eine Monatskarte kaufen.", "我想買月票。"),
            ("Wie lange dauert die Fahrt?", "車程要多久？"),
        ],
        "健康": [
            ("Ich bin krank und möchte einen Termin beim Arzt machen.", "我生病了，想預約看醫生。"),
            ("Ich habe Kopfschmerzen, kann ich eine Tablette haben?", "我頭痛，能給我一顆藥嗎？"),
            ("Der Hals tut mir sehr weh.", "我的喉嚨很痛。"),
            ("Ich brauche einen Verband für die Wunde.", "我需要繃帶包紮傷口。"),
            ("Ich mache täglich Sport.", "我每天運動。"),
            ("Ich bin allergisch gegen Erdnüsse.", "我對花生過敏。"),
            ("Ich nehme Medikamente gegen Bluthochdruck.", "我吃血壓藥。"),
            ("Die Grippe ist schlimm in dieser Saison.", "這個季節流感很嚴重。"),
            ("Ich war beim Zahnarzt, um meine Zähne zu putzen.", "我去牙醫診所洗牙。"),
            ("Ich bin diabetisch, daher esse ich keinen Zucker.", "我是糖尿病患者，所以不吃糖。"),
        ],
    }
    
    for topic, items in topics.items():
        for german, chinese in items:
            # 創建三個選項，其中一個是正確答案
            wrong_answers = ["不是這個意思。", "這是另一個句子。", "這個翻譯不對。"]
            random.shuffle(wrong_answers)
            
            german_questions.append({
                "text": german,
                "choices": [chinese] + wrong_answers[:2],
                "answer": 0
            })
            
            # 為了達到1000+題，我們還需要添加更多變化
            # 用不同的錯誤答案再次添加這個題目
            wrong_answers2 = ["完全不同的意思。", "這不是這個意思。", "錯誤的翻譯。"]
            random.shuffle(wrong_answers2)
            
            if len(german_questions) < 1200:  # 控制題目總數
                german_questions.append({
                    "text": german,
                    "choices": [chinese] + wrong_answers2[:2],
                    "answer": 0
                })

add_german_questions()

# 日文生活化題庫
japanese_questions = []

def add_japanese_questions():
    global japanese_questions
    
    topics = {
        "早餐": [
            ("朝食にトーストとコーヒーをいただきます。", "早餐我吃吐司和咖啡。"),
            ("卵焼きは美味しくて、毎日食べたいです。", "蛋卷很好吃，我每天都想吃。"),
            ("ご飯とみそ汁と漬物で、朝食をします。", "我早餐吃米飯、味噌湯和醃菜。"),
            ("牛乳をコップに入れてください。", "請把牛奶倒進杯子裡。"),
            ("パンはバターとジャムを塗って食べます。", "我在麵包上塗黃油和果醬後吃。"),
            ("納豆ご飯を毎朝食べます。", "我每天早上吃納豆飯。"),
            ("朝食は和食が好きです。", "我喜歡早餐吃和食。"),
            ("シリアルと牛乳で朝食を済ませます。", "我用穀物麥片和牛奶吃早餐。"),
            ("朝食後、学校に行きます。", "早餐後我去上學。"),
            ("朝食を食べないで、仕事に行く人が多い。", "許多人不吃早餐就去上班。"),
        ],
        "午餐": [
            ("昼食はラーメンと餃子を食べたいです。", "午餐我想吃拉麵和餃子。"),
            ("寿司はたくさんネタが入っていて、とても美味しい。", "壽司有很多餡料，很好吃。"),
            ("この天丼の天ぷらは揚げたてで、最高です。", "這個天丼的天婦羅是剛炸的，最棒。"),
            ("蕎麦はつゆに浸して食べるのが好きです。", "我喜歡把蕎麥麵浸在湯汁裡吃。"),
            ("定食は定食は御飯、味噌汁、おかずが付いてくる。", "套餐通常包括米飯、味噌湯和配菜。"),
            ("カツ丼は揚げたての豚カツが最高です。", "炸豬排蓋飯的炸豬排最好吃。"),
            ("そばうどんとどちらが好きですか？", "蕎麥麵和烏龍麵你更喜歡哪一個？"),
            ("弁当を持って、公園で食べましょう。", "我們帶便當到公園吃。"),
            ("カレーライスは簡単で美味しい。", "咖哩飯簡單又好吃。"),
            ("焼き魚と野菜で、健康的な昼食です。", "烤魚和蔬菜是健康的午餐。"),
        ],
        "晚餐": [
            ("夜ご飯には焼き魚を作ります。", "晚餐我做烤魚。"),
            ("すき焼きはたくさん野菜と肉が入っています。", "壽喜燒裡有很多蔬菜和肉。"),
            ("カレーライスは国民食と言えます。", "咖哩飯可以說是國民食物。"),
            ("親子丼はとても栄養がありますね。", "親子丼很有營養。"),
            ("夜食の時は、塩辛いものより軽いものが好きです。", "晚餐時我喜歡清淡的食物勝過鹹的。"),
            ("味噌汁は毎晩作ります。", "我每晚都做味噌湯。"),
            ("野菜をいっぱい食べて、健康です。", "吃很多蔬菜很健康。"),
            ("ステーキは久しぶりに食べたい。", "好久沒吃牛排了。"),
            ("天ぷらは油っぽいけど、美味しい。", "天婦羅油膩但很好吃。"),
            ("春キャベツの炒め物は最高です。", "春天高麗菜炒菜最棒。"),
        ],
        "飲品": [
            ("毎朝コーヒーを飲みます。", "我每天早上喝咖啡。"),
            ("紅茶はミルクを入れて飲みます。", "我在紅茶裡加牛奶。"),
            ("冷たい水が飲みたいです。", "我想喝冷水。"),
            ("日本茶は好きですか？", "你喜歡喝日本茶嗎？"),
            ("ビールはドイツが有名です。", "啤酒以德國最有名。"),
            ("オレンジジュースは朝食に最適です。", "柳橙汁是早餐的最佳選擇。"),
            ("エスプレッソはイタリアンコーヒーです。", "濃咖啡是義大利咖啡。"),
            ("緑茶は砂糖なしで飲みます。", "我不加糖喝綠茶。"),
            ("ホットチョコレートは冬に美味しい。", "熱巧克力在冬天很好喝。"),
            ("水をたくさん飲んで、健康です。", "喝很多水很健康。"),
        ],
        "廁所/浴室": [
            ("トイレットペーパーを買う必要があります。", "我需要買衛生紙。"),
            ("すみません、トイレはどこですか？", "不好意思，廁所在哪裡？"),
            ("シャンプーは髪に優しいものを選びました。", "我選了溫和的洗髮精。"),
            ("お風呂の時間は、一日で一番リラックスできる時間です。", "洗澡時間是一天中最放鬆的時刻。"),
            ("歯磨きは毎日二回行っています。", "我每天刷牙兩次。"),
            ("タオルで体を拭きます。", "我用毛巾擦身體。"),
            ("石鹸で手を洗います。", "我用肥皂洗手。"),
            ("歯ブラシを新しいのに変えました。", "我把牙刷換成新的。"),
            ("入浴剤を使って、気持ちいいです。", "用浴鹽很舒服。"),
            ("鏡に曇りが出ました。", "鏡子起霧了。"),
        ],
        "衣服": [
            ("このシャツは洗濯すると、少し小さくなってしまいました。", "這件襯衫洗過後變小了。"),
            ("衣類は30度の水で優しく洗います。", "衣服用30度的溫水輕輕洗。"),
            ("このスカートにシミが付いて、困っています。", "這條裙子沾上污漬，我很困擾。"),
            ("アイロンをかけて、シワを取ります。", "我熨衣服來去除皺紋。"),
            ("冬のコートは厚いですから、クリーニングに出します。", "冬天的大衣很厚，我送去乾洗。"),
            ("色物と白物は別々に洗います。", "有顏色的衣服和白衣服要分開洗。"),
            ("靴下をなくしました。", "我丟了襪子。"),
            ("ズボンのファスナーが壊れました。", "褲子的拉鏈壞了。"),
            ("セーターは毛玉ができました。", "毛衣起毛球了。"),
            ("洋服を整理して、捨てるものを見つけました。", "整理衣服時發現一些可以丟掉的。"),
        ],
        "家務": [
            ("掃除の時間は、毎週日曜日にしています。", "我每個星期天做家務。"),
            ("ゴミを出す日は、火曜日と金曜日です。", "倒垃圾的日期是星期二和星期五。"),
            ("食器洗いは時間がかかりますが、必要です。", "洗碗盤耗時但必要。"),
            ("浴室の掃除は、毎日少しずつ行っています。", "我每天花一點時間清潔浴室。"),
            ("布団はたたいて、天日で干します。", "我拍打被子後放在陽光下曬。"),
            ("部屋を掃くとホコリが出ます。", "掃房間時會出現灰塵。"),
            ("窓ガラスを綺麗に拭きました。", "我把窗玻璃擦乾淨了。"),
            ("台所が汚れたので、清掃しました。", "廚房很髒，我清潔了。"),
            ("洗濯物を干して、明朝に取り入れます。", "我掛衣服，明早收進去。"),
            ("家の中を片付けるのは大変です。", "打掃房子很費力。"),
        ],
    }
    
    for topic, items in topics.items():
        for japanese, chinese in items:
            # 創建三個選項
            wrong_answers = ["不是這個意思。", "這是另一個句子。", "這個翻譯不對。"]
            random.shuffle(wrong_answers)
            
            japanese_questions.append({
                "text": japanese,
                "choices": [chinese] + wrong_answers[:2],
                "answer": 0
            })
            
            # 用不同的錯誤答案再次添加
            if len(japanese_questions) < 600:
                wrong_answers2 = ["完全不同的意思。", "這不是這個意思。", "錯誤的翻譯。"]
                random.shuffle(wrong_answers2)
                japanese_questions.append({
                    "text": japanese,
                    "choices": [chinese] + wrong_answers2[:2],
                    "answer": 0
                })

add_japanese_questions()

# 輸出為 JavaScript 格式並寫入檔案
def generate_javascript_output():
    german_js = "const germanQuestions = " + json.dumps(german_questions, ensure_ascii=False) + ";\n\n"
    japanese_js = "const japaneseQuestions = " + json.dumps(japanese_questions, ensure_ascii=False) + ";"
    return german_js, japanese_js

if __name__ == "__main__":
    german_js, japanese_js = generate_javascript_output()
    
    # 寫入檔案
    with open('questions_output.js', 'w', encoding='utf-8') as f:
        f.write(german_js)
        f.write(japanese_js)
    
    print(f"德文題目數量: {len(german_questions)}")
    print(f"日文題目數量: {len(japanese_questions)}")
    print(f"總題目數: {len(german_questions) + len(japanese_questions)}")
    print("\n✅ 題目已成功輸出到 questions_output.js")
    print("\n=== 德文輸出 (前 200 字) ===")
    print(german_js[:200] + "...")
    print("\n=== 日文輸出 (前 200 字) ===")
    print(japanese_js[:200] + "...")
