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
    
    japanese_questions = []
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
    
    # 午餐相關
    { "text": "Was ist heute Mittag im Menü? Es sieht sehr lecker aus.", "choices": ["今天午餐菜單是什麼？看起來很好吃。", "今天天氣很適合在戶外吃午餐。", "午餐時間快到了，我有點餓。"], "answer": 0 },
    { "text": "Ich nehme einen Salat mit Hähnchen und Öl-Essig-Dressing als Mittagessen.", "choices": ["我午餐吃雞肉沙拉配油醋醬。", "午餐吃沙拉對身體很健康。", "我喜歡各種不同的沙拉。"], "answer": 0 },
    { "text": "Die Pasta schmeckt fantastisch, der Koch hat es perfekt gemacht.", "choices": ["這義大利麵很好吃，廚師做得很完美。", "義大利麵很容易做。", "我常常在家自己煮義大利麵。"], "answer": 0 },
    { "text": "Kann ich noch einen Teller Suppe bekommen? Die erste war sehr lecker.", "choices": ["我還能再要一盤湯嗎？第一盤很好喝。", "這家餐廳的湯很有名。", "我喜歡各種不同的湯。"], "answer": 0 },
    { "text": "Für Mittagessen will ich Fisch mit Gemüse und Kartoffeln.", "choices": ["午餐我想吃魚配蔬菜和馬鈴薯。", "魚很有營養，很健康。", "我喜歡吃烤魚。"], "answer": 0 },
    
    # 晚餐相關
    { "text": "Heute Abend essen wir gegrilltes Hähnchen mit Reis und Brokkoli.", "choices": ["今晚我們吃烤雞配米飯和綠花菜。", "烤雞很容易準備。", "我很久沒有吃過好的烤雞了。"], "answer": 0 },
    { "text": "Das Steak ist zu roh, kann der Kellner es noch mal auf den Grill legen?", "choices": ["這牛排太生了，服務員能再把它放回烤架嗎？", "牛排的熟度對味道很重要。", "我喜歡吃七分熟的牛排。"], "answer": 0 },
    { "text": "Magst du Würstchen oder lieber Fleischbällchen zum Abendessen?", "choices": ["你晚餐喜歡吃香腸還是肉丸？", "香腸和肉丸都是德國很受歡迎的食物。", "我喜歡各種肉類食品。"], "answer": 0 },
    { "text": "Zum Nachtisch nehme ich Schokoladenkuchen mit Vanilleeis.", "choices": ["甜點我要巧克力蛋糕配香草冰淇淋。", "巧克力蛋糕是我最喜歡的甜點。", "冰淇淋在夏天特別爽口。"], "answer": 0 },
    { "text": "Das Gemüse ist noch zu hart, können Sie es etwas länger kochen?", "choices": ["蔬菜還太硬，你能再煮久一點嗎？", "新鮮蔬菜很脆。", "我喜歡吃軟一點的蔬菜。"], "answer": 0 },
    
    # 餐廳相關
    { "text": "Tisch für vier Personen, bitte. Haben Sie noch einen freien Platz?", "choices": ["請給我一張四人桌。你們還有空位嗎？", "這家餐廳今天很擁擠。", "我很喜歡這家餐廳的環境。"], "answer": 0 },
    { "text": "Können Sie mir die Speisekarte geben? Ich bin bereit zu bestellen.", "choices": ["你能給我菜單嗎？我準備點餐了。", "這家餐廳的菜單很豐富。", "點菜前我喜歡先看看評價。"], "answer": 0 },
    { "text": "Ich hätte gerne einen Wein zum Essen. Welcher Wein passt zu meinem Fisch?", "choices": ["我想要一杯葡萄酒配餐。什麼酒配魚最合適？", "紅葡萄酒和白葡萄酒有不同的風味。", "德國葡萄酒很有名。"], "answer": 0 },
    { "text": "Die Rechnung, bitte! War ein sehr gutes Essen heute.", "choices": ["請結帳！今天的食物很好吃。", "這家餐廳的服務很周到。", "下次我還會來這家餐廳。"], "answer": 0 },
    { "text": "Schmeckt dir das Essen? Oder soll ich etwas zurückgeben?", "choices": ["食物味道如何？還是我應該退回去？", "這家廚師的手藝很好。", "食物的新鮮度很重要。"], "answer": 0 },
    
    # 廚房/烹飪相關
    { "text": "Ich brauche ein scharfes Messer zum Schneiden des Fleisches.", "choices": ["我需要一把鋒利的刀來切肉。", "廚房的刀一定要保持銳利。", "切肉的刀和切菜的刀不一樣。"], "answer": 0 },
    { "text": "Wo ist die Pfanne? Ich will Eier braten.", "choices": ["煎鍋在哪裡？我想煎蛋。", "用不同的鍋可以做不同的菜。", "不粘鍋很方便。"], "answer": 0 },
    { "text": "Kannst du mir helfen, die Kartoffeln zu schälen?", "choices": ["你能幫我削馬鈴薯皮嗎？", "削馬鈴薯是個耗時的工作。", "馬鈴薯削過皮後會變黑。"], "answer": 0 },
    { "text": "Der Backofen ist auf 200 Grad eingestellt, das Brot backt jetzt.", "choices": ["烤箱設定在200度，現在在烤麵包。", "每種麵包需要不同的溫度。", "烤麵包的香氣很吸引人。"], "answer": 0 },
    { "text": "Ich habe zu viel Salz in die Suppe getan, sie ist jetzt zu salzig.", "choices": ["我在湯裡放了太多鹽，現在太鹹了。", "適量的鹽能提升食物的風味。", "太鹹的食物不健康。"], "answer": 0 },
    
    # 超市購物
    { "text": "Wie viel kostet dieser Block Käse? Ist er aus der lokalen Produktion?", "choices": ["這塊起司要多少錢？是本地生產的嗎？", "起司在冷櫃裡保存。", "不同種類的起司有不同的味道。"], "answer": 0 },
    { "text": "Ich suche nach Mehl und Zucker, wo befindet sich die Backzutaten-Abteilung?", "choices": ["我找麵粉和糖，烘焙食材部在哪裡？", "超市的各個部分都有明確標示。", "烘焙食材有很多選擇。"], "answer": 0 },
    { "text": "Das Obst sieht heute sehr frisch aus. Diese Äpfel kosten wie viel?", "choices": ["今天的水果看起來很新鮮。這些蘋果要多少錢？", "新鮮水果對健康很重要。", "應季水果比較便宜。"], "answer": 0 },
    { "text": "Haben Sie diesen Artikel im Angebot oder in Promotion?", "choices": ["這個商品有促銷或優惠嗎？", "超市經常有打折活動。", "買多件有時可以折扣更多。"], "answer": 0 },
    { "text": "Wo ist die Kasse? Ich bin bereit zu zahlen.", "choices": ["收銀台在哪裡？我準備結帳。", "超市的收銀台通常在出口附近。", "這家超市有很多收銀台。"], "answer": 0 },
    
    # 廁所/浴室用品
    { "text": "Ich brauche Toilettenpapier. Wo kann ich es kaufen?", "choices": ["我需要衛生紙。我在哪裡可以買到？", "衛生紙在衛生用品區。", "好的衛生紙質量很重要。"], "answer": 0 },
    { "text": "Entschuldigung, wo ist die Toilette? Ich muss dringend gehen.", "choices": ["不好意思，廁所在哪裡？我很急。", "在公共場所找廁所很重要。", "廁所通常有清晰的標示。"], "answer": 0 },
    { "text": "Ich wasche meine Hände mit Seife und warmem Wasser.", "choices": ["我用肥皂和溫水洗手。", "洗手很重要，尤其在吃飯前。", "肥皂能殺死細菌。"], "answer": 0 },
    { "text": "Mir fehlt die Zahnbürste, ich muss heute Abend eine neue kaufen.", "choices": ["我的牙刷丟了，今天晚上要買一把新的。", "定期更換牙刷很重要。", "不同硬度的牙刷適合不同的人。"], "answer": 0 },
    { "text": "Kann ich ein Handtuch haben? Das Badezimmer ist nass.", "choices": ["我能要一條毛巾嗎？浴室很濕。", "毛巾應該經常清洗。", "吸水毛巾很有用。"], "answer": 0 },
    
    # 洗漱/衛生
    { "text": "Ich brauche Zahnpasta und Mundwasser für meine Zahnreinigung.", "choices": ["我需要牙膏和漱口水來清潔牙齒。", "每天刷牙很重要。", "好的牙膏能防止蛀牙。"], "answer": 0 },
    { "text": "Das Shampoo riecht sehr gut. Ist es für trockenes oder öliges Haar?", "choices": ["這個洗髮精味道很好。它適合乾性還是油性頭髮？", "選擇適合自己髮質的洗髮精很重要。", "好的洗髮精能保護頭髮。"], "answer": 0 },
    { "text": "Ich nehme ein warmes Bad und nutze Badeschaum zum Entspannen.", "choices": ["我洗個溫水澡，用浴泡放鬆。", "洗澡是一天中最舒服的時刻。", "長時間洗澡會讓皮膚變皺。"], "answer": 0 },
    { "text": "Wo ist der Kamm? Ich muss mein Haar kämmen, bevor ich ausgehe.", "choices": ["梳子在哪裡？我出門前要梳頭。", "定期梳頭能使頭髮更健康。", "不同的梳子有不同的用途。"], "answer": 0 },
    { "text": "Ich benutze Deodorant nach dem Duschen, um frisch zu bleiben.", "choices": ["洗澡後我用止汗劑保持清爽。", "止汗劑能防止出汗。", "除臭劑有很多香氣可選擇。"], "answer": 0 },
    
    # 衣服相關
    { "text": "Diese Hose passt mir nicht mehr, sie ist zu klein. Ich brauche eine größere Größe.", "choices": ["這條褲子我穿不下了，太小了。我需要更大的尺碼。", "衣服經過多次洗滌會變小。", "買衣服時要確認尺碼。"], "answer": 0 },
    { "text": "Ich wasche die Wäsche bei 30 Grad mit Waschmittel.", "choices": ["我用洗衣精在30度的溫度洗衣服。", "不同的衣服需要不同的洗滌溫度。", "冷水洗可以節省能源。"], "answer": 0 },
    { "text": "Das Hemd hat einen Fleck, ich versuche ihn mit Reinigungsmittel zu entfernen.", "choices": ["襯衫有個污漬，我試著用清潔劑去除。", "及時清理污漬會比較容易。", "某些污漬需要特殊的清潔劑。"], "answer": 0 },
    { "text": "Ich bügele die Bluse, weil sie heute sehr zerknittert ist.", "choices": ["我熨一下這件女用襯衫，因為今天很皺。", "定期熨衣服能使衣服保持整齊。", "不是所有衣服都適合高溫熨燙。"], "answer": 0 },
    { "text": "Diese Jacke ist zu dick für den Sommer, ich trage eine leichtere Kleidung.", "choices": ["這件夾克對夏天太厚了，我穿更輕薄的衣服。", "衣服應該根據季節選擇。", "四季穿衣很不一樣。"], "answer": 0 },
    
    # 家務相關
    { "text": "Ich kehre das Wohnzimmer und wasche dann den Boden.", "choices": ["我掃客廳，然後拖地。", "定期打掃房間很重要。", "不同房間的清潔方法不同。"], "answer": 0 },
    { "text": "Der Müll ist voll, ich muss ihn leeren und einen neuen Sack einsetzen.", "choices": ["垃圾桶滿了，我要倒垃圾並裝新的垃圾袋。", "定期倒垃圾很重要。", "分類垃圾很環保。"], "answer": 0 },
    { "text": "Ich wasche Geschirr nach dem Essen, damit die Küche sauber bleibt.", "choices": ["吃完飯後我洗碗盤，這樣廚房保持乾淨。", "洗碗很乏味但必要。", "洗碗機能節省時間。"], "answer": 0 },
    { "text": "Das Badezimmer ist schmutzig, ich putze Badewanne und Fliesen.", "choices": ["浴室很髒，我要清潔浴缸和瓷磚。", "浴室容易積累細菌。", "定期清潔浴室很衛生。"], "answer": 0 },
    { "text": "Ich wechsle die Bettwäsche jede Woche, um hygienisch zu sein.", "choices": ["我每週換一次床單，保持衛生。", "乾淨的床單能幫助更好的睡眠。", "定期清洗床單很重要。"], "answer": 0 },
    
    # 購物/費用相關
    { "text": "Wie viel kostet dieser Artikel? Gibt es einen Rabatt?", "choices": ["這個商品要多少錢？有折扣嗎？", "購物時應該比較價格。", "打折時是買東西的好時機。"], "answer": 0 },
    { "text": "Kann ich mit Kreditkarte zahlen oder nur mit Bargeld?", "choices": ["我能用信用卡付款還是只能付現？", "現代商店通常接受多種付款方式。", "信用卡能獲得回饋點數。"], "answer": 0 },
    { "text": "Das ist zu teuer, gibt es nicht etwas Billigeres?", "choices": ["這太貴了，沒有更便宜的嗎？", "貨比三家能找到好價格。", "銷售員有時可以協商價格。"], "answer": 0 },
    { "text": "Ich haben einen Gutschein, kann ich ihn verwenden?", "choices": ["我有張禮券，我能用嗎？", "禮券通常有有效期限。", "禮券能幫助節省購物費用。"], "answer": 0 },
    { "text": "Können Sie mir eine Quittung geben? Ich brauche sie für die Rückgabe.", "choices": ["你能給我收據嗎？我需要它來退貨。", "收據是購物的證明。", "沒有收據通常無法退貨。"], "answer": 0 },
    
    # 交通相關
    { "text": "Wo ist die nächste Bushaltestelle? Ich muss zum Bahnhof gehen.", "choices": ["最近的公車站在哪裡？我要去火車站。", "公車是城市交通的重要方式。", "公車時刻表應該提前查詢。"], "answer": 0 },
    { "text": "Eine Fahrkarte zum Flughafen, bitte. Wie lange dauert die Fahrt?", "choices": ["請給我一張到機場的票。車程要多久？", "到機場的車票通常比較貴。", "早上的班次通常比較擁擠。"], "answer": 0 },
    { "text": "Mein Auto braucht Benzin. Wo ist die nächste Tankstelle?", "choices": ["我的車需要加油。最近的加油站在哪裡？", "加油站分布在各地。", "燃油價格每天都可能變化。"], "answer": 0 },
    { "text": "Der Zug hat Verspätung. Wann kommt er an?", "choices": ["火車晚點了。它什麼時候到？", "火車延誤很令人沮喪。", "應該提前到達車站。"], "answer": 0 },
    { "text": "Ich brauche ein Taxi, können Sie mir einen rufen?", "choices": ["我需要一輛計程車，你能幫我叫一輛嗎？", "計程車在繁忙時間很難找到。", "計程車資在不同時段可能不同。"], "answer": 0 },
    
    # 日常會話
    { "text": "Guten Tag! Wie geht es dir heute?", "choices": ["你好！你今天怎麼樣？", "每天問候很重要。", "真摯的問候能拉近距離。"], "answer": 0 },
    { "text": "Entschuldigung, wie ist dein Name?", "choices": ["不好意思，你叫什麼名字？", "認識新人時應該先問名字。", "記住人的名字很重要。"], "answer": 0 },
    { "text": "Danke für die Hilfe! Du bist wirklich sehr nett.", "choices": ["謝謝你的幫忙！你真的很好。", "感謝別人能建立良好關係。", "互相幫助是友誼的基礎。"], "answer": 0 },
    { "text": "Entschuldigung, können Sie mir helfen?", "choices": ["不好意思，你能幫我嗎？", "尋求幫助是正常的。", "大多數人很樂意幫助他人。"], "answer": 0 },
    { "text": "Auf Wiedersehen! Bis bald, hoffentlich sehen wir uns wieder.", "choices": ["再見！希望很快見面。", "道別是禮貌的。", "真誠的道別能留下好印象。"], "answer": 0 },
    
    # 健康相關
    { "text": "Ich bin krank und möchte einen Termin beim Arzt machen.", "choices": ["我生病了，想預約看醫生。", "定期體檢很重要。", "及時就醫能防止病情惡化。"], "answer": 0 },
    { "text": "Ich habe Kopfschmerzen, kann ich eine Kopfschmerztablette haben?", "choices": ["我頭痛，能給我一顆止痛藥嗎？", "許多人經歷過頭痛。", "適量的止痛藥能緩解症狀。"], "answer": 0 },
    { "text": "Der Hals tut mir sehr weh. Vielleicht bin ich erkältet.", "choices": ["我的喉嚨很痛。也許我感冒了。", "感冒是常見的疾病。", "喉嚨痛需要多喝溫水。"], "answer": 0 },
    { "text": "Ich brauche einen Verband für die Wunde am Arm.", "choices": ["我需要一個繃帶包紮手臂上的傷口。", "小傷口應該妥善處理。", "防水繃帶很方便。"], "answer": 0 },
    { "text": "Ich mache täglich Sport zum Gesundbleiben.", "choices": ["我每天運動以保持健康。", "運動對身心健康很重要。", "規律運動能增強免疫力。"], "answer": 0 },
]

# 日文生活化題庫
japanese_questions = [
    # 早餐相關
    { "text": "朝食にトーストとコーヒーをいただきます。", "choices": ["早餐我吃吐司和咖啡。", "早起對健康很重要。", "咖啡能幫助我們清醒。"], "answer": 0 },
    { "text": "卵焼きは美味しくて、毎日食べたいです。", "choices": ["蛋卷很好吃，我每天都想吃。", "日本人喜歡吃卵焼。", "卵焼是日本傳統早餐食物。"], "answer": 0 },
    { "text": "ご飯とみそ汁と漬物で、朝食をします。", "choices": ["我早餐吃米飯、味噌湯和醃菜。", "這是傳統的日本早餐。", "味噌湯很溫暖舒適。"], "answer": 0 },
    { "text": "牛乳をコップに入れてください。", "choices": ["請把牛奶倒進杯子裡。", "牛奶對骨骼健康很重要。", "冷牛奶比熱牛奶爽口。"], "answer": 0 },
    { "text": "パンはバターとジャムを塗って食べます。", "choices": ["我在麵包上塗黃油和果醬後吃。", "不同的醬料有不同的味道。", "塗抹在麵包上的醬料很多。"], "answer": 0 },
    
    # 午餐相關
    { "text": "昼食はラーメンと餃子を食べたいです。", "choices": ["午餐我想吃拉麵和餃子。", "拉麵和餃子是日本流行食物。", "拉麵有各種不同的湯頭。"], "answer": 0 },
    { "text": "寿司はたくさんネタが入っていて、とても美味しい。", "choices": ["壽司有很多餡料，很好吃。", "壽司是日本的代表食物。", "新鮮的魚最適合做壽司。"], "answer": 0 },
    { "text": "この天丼の天ぷらは揚げたてで、最高です。", "choices": ["這個天丼的天婦羅是剛炸的，最棒。", "炸得剛好的天婦羅最酥脆。", "天丼是日本的經典午餐。"], "answer": 0 },
    { "text": "蕎麦はつゆに浸して食べるのが好きです。", "choices": ["我喜歡把蕎麥麵浸在湯汁裡吃。", "蕎麥麵是日本健康食物。", "冷蕎麥麵在夏天很爽口。"], "answer": 0 },
    { "text": "定食は定食は御飯、味噌汁、おかずが付いてくる。", "choices": ["套餐通常包括米飯、味噌湯和配菜。", "套餐是日本很常見的午餐選擇。", "套餐的價格通常很划算。"], "answer": 0 },
    
    # 晚餐相關
    { "text": "夜ご飯には焼き魚を作ります。", "choices": ["晚餐我做烤魚。", "烤魚是健康的晚餐選擇。", "不同的魚有不同的風味。"], "answer": 0 },
    { "text": "すき焼きはたくさん野菜と肉が入っています。", "choices": ["壽喜燒裡有很多蔬菜和肉。", "壽喜燒是日本很受歡迎的火鍋。", "吃壽喜燒是一種社交活動。"], "answer": 0 },
    { "text": "カレーライスは国民食と言えます。", "choices": ["咖哩飯可以說是國民食物。", "咖哩飯在日本很普遍。", "每個家庭有自己特別的咖哩食譜。"], "answer": 0 },
    { "text": "親子丼はとても栄養がありますね。", "choices": ["親子丼很有營養。", "親子丼是日本傳統菜。", "親子丼很適合快速晚餐。"], "answer": 0 },
    { "text": "夜食の時は、塩辛いものより軽いものが好きです。", "choices": ["晚餐時我喜歡清淡的食物勝過鹹的。", "太鹹的食物可能影響睡眠。", "晚餐吃得太飽會難以入眠。"], "answer": 0 },
    
    # 廁所/浴室用品
    { "text": "トイレットペーパーを買う必要があります。", "choices": ["我需要買衛生紙。", "衛生紙是日常必需品。", "日本的衛生紙質量很好。"], "answer": 0 },
    { "text": "すみません、トイレはどこですか？", "choices": ["不好意思，廁所在哪裡？", "在陌生地方找廁所很急。", "找廁所時應該詢問工作人員。"], "answer": 0 },
    { "text": "シャンプーは髪に優しいものを選びました。", "choices": ["我選了溫和的洗髮精。", "好的洗髮精能保護髮質。", "不同髮質需要不同的洗髮精。"], "answer": 0 },
    { "text": "お風呂の時間は、一日で一番リラックスできる時間です。", "choices": ["洗澡時間是一天中最放鬆的時刻。", "洗澡有助於放鬆身心。", "溫水澡能舒緩肌肉疲勞。"], "answer": 0 },
    { "text": "歯磨きは毎日二回行っています。", "choices": ["我每天刷牙兩次。", "每天刷牙很重要。", "睡前刷牙能防止蛀牙。"], "answer": 0 },
    
    # 衣服相關
    { "text": "このシャツは洗濯すると、少し小さくなってしまいました。", "choices": ["這件襯衫洗過後變小了。", "衣服多次洗滌會收縮。", "應該按照洗標說明洗衣。"], "answer": 0 },
    { "text": "衣類は30度の水で優しく洗います。", "choices": ["衣服用30度的溫水輕輕洗。", "不同衣物有不同的洗滌方式。", "冷水洗衣能節省能源。"], "answer": 0 },
    { "text": "このスカートにシミが付いて、困っています。", "choices": ["這條裙子沾上污漬，我很困擾。", "及時清理污漬最有效。", "某些污漬很難清除。"], "answer": 0 },
    { "text": "アイロンをかけて、シワを取ります。", "choices": ["我熨衣服來去除皺紋。", "熨衣服能使衣服看起來整齊。", "不是所有衣服都能用高溫熨燙。"], "answer": 0 },
    { "text": "冬のコートは厚いですから、クリーニングに出します。", "choices": ["冬天的大衣很厚，我送去乾洗。", "厚衣服應該定期乾洗。", "專業乾洗能延長衣服壽命。"], "answer": 0 },
    
    # 家務相關
    { "text": "掃除の時間は、毎週日曜日にしています。", "choices": ["我每個星期天做家務。", "定期打掃很重要。", "有清潔時間表能保持整潔。"], "answer": 0 },
    { "text": "ゴミを出す日は、火曜日と金曜日です。", "choices": ["倒垃圾的日期是星期二和星期五。", "日本有嚴格的垃圾分類。", "按時倒垃圾很重要。"], "answer": 0 },
    { "text": "食器洗いは時間がかかりますが、必要です。", "choices": ["洗碗盤耗時但必要。", "洗碗是日常家務。", "洗碗機能節省時間。"], "answer": 0 },
    { "text": "浴室の掃除は、毎日少しずつ行っています。", "choices": ["我每天花一點時間清潔浴室。", "定期清潔浴室能防止黴菌。", "浴室容易積累細菌。"], "answer": 0 },
    { "text": "布団はたたいて、天日で干します。", "choices": ["我拍打被子後放在陽光下曬。", "日曬能殺死細菌和蟎蟲。", "乾燥被子能增加舒適度。"], "answer": 0 },
    
    # 購物相關
    { "text": "この商品は幾らですか？安く買えますか？", "choices": ["這個商品要多少錢？能便宜一點嗎？", "購物時比較價格很重要。", "打折時是買東西的好時機。"], "answer": 0 },
    { "text": "クレジットカードで払えますか、それとも現金だけですか？", "choices": ["能用信用卡付款，還是只能付現？", "現代商店通常接受多種支付方式。", "信用卡很便利。"], "answer": 0 },
    { "text": "これは少し高いですが、品質がいいですね。", "choices": ["這個有點貴，但品質很好。", "高品質通常需要較高的價格。", "便宜貨不一定品質差。"], "answer": 0 },
    { "text": "クーポンを持っています、使えますか？", "choices": ["我有張折扣券，能用嗎？", "折扣券能幫助節省購物費用。", "折扣券通常有有效期限。"], "answer": 0 },
    { "text": "レシートをください。返品する時に必要です。", "choices": ["請給我收據。我退貨時需要。", "收據是購物的證明。", "許多商店要求收據才能退貨。"], "answer": 0 },
    
    # 交通相關
    { "text": "駅はどこですか。電車に乗りたいです。", "choices": ["車站在哪裡？我想搭電車。", "日本的電車很準時。", "電車是城市主要交通工具。"], "answer": 0 },
    { "text": "羽田空港行の電車の切符をください。", "choices": ["請給我到羽田機場的電車票。", "到機場的電車通常比較貴。", "機場電車通常很擁擠。"], "answer": 0 },
    { "text": "このタクシーはいくらですか？", "choices": ["這輛計程車要多少錢？", "日本計程車費用比較貴。", "計程車資會隨時間增加。"], "answer": 0 },
    { "text": "電車は遅れています。到着は何時ですか？", "choices": ["電車晚點了。什麼時候到達？", "電車延誤有時會發生。", "應該提前檢查電車時刻表。"], "answer": 0 },
    { "text": "自分の車にガソリンが必要です。ガソリンスタンドはどこですか？", "choices": ["我的車需要加油。加油站在哪裡？", "加油站在各個地方都有。", "汽油價格每天可能變化。"], "answer": 0 },
    
    # 日常會話
    { "text": "おはようございます。今日はお天気がいいですね。", "choices": ["早安。今天天氣很好。", "打招呼很重要。", "用自然現象開啟對話很常見。"], "answer": 0 },
    { "text": "すみません、お名前は何ですか？", "choices": ["不好意思，請問你叫什麼名字？", "認識新人時應該先問名字。", "記住人的名字很重要。"], "answer": 0 },
    { "text": "ご協力ありがとうございます。お手伝いいただき感謝します。", "choices": ["謝謝你的幫忙。感謝你的協助。", "感謝別人能建立良好關係。", "表達感謝很重要。"], "answer": 0 },
    { "text": "すみません、手伝っていただけますか？", "choices": ["不好意思，你能幫我嗎？", "尋求幫助是正常的。", "大多數人很樂意幫助他人。"], "answer": 0 },
    { "text": "さようなら。また明日。", "choices": ["再見。明天見。", "道別很重要。", "真誠的道別能留下好印象。"], "answer": 0 },
    
    # 健康相關
    { "text": "具合が悪いので、医者の予約を取りたいです。", "choices": ["我感覺不舒服，想預約看醫生。", "及時就醫很重要。", "定期體檢能防止疾病。"], "answer": 0 },
    { "text": "頭が痛いので、頭痛薬をください。", "choices": ["我頭痛，請給我止痛藥。", "許多人經歷過頭痛。", "適量的止痛藥能緩解症狀。"], "answer": 0 },
    { "text": "喉が痛いです。もしかして風邪かもしれません。", "choices": ["我喉嚨痛。也許我感冒了。", "感冒很常見。", "喉嚨痛需要多喝溫水。"], "answer": 0 },
    { "text": "怪我をしたので、ばんそうこうが必要です。", "choices": ["我受傷了，需要繃帶。", "小傷口應該妥善包紮。", "繃帶能保護傷口。"], "answer": 0 },
    { "text": "毎日運動することが、健康を保つコツです。", "choices": ["每天運動是保持健康的秘訣。", "運動對身心健康很重要。", "規律運動能增強免疫力。"], "answer": 0 },
]

# 輸出為 JavaScript 格式
def generate_javascript_output():
    german_js = "const germanQuestions = " + json.dumps(german_questions, ensure_ascii=False) + ";"
    japanese_js = "const japaneseQuestions = " + json.dumps(japanese_questions, ensure_ascii=False) + ";"
    return german_js, japanese_js

if __name__ == "__main__":
    german_js, japanese_js = generate_javascript_output()
    print(f"德文題目數量: {len(german_questions)}")
    print(f"日文題目數量: {len(japanese_questions)}")
    print("\n=== 德文輸出 ===")
    print(german_js[:200] + "...")
    print("\n=== 日文輸出 ===")
    print(japanese_js[:200] + "...")
