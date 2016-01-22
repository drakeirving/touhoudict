import sys

touhou = {
	"characters": {
		"古明地 こいし": "Koishi Komeiji",
		"博麗 霊夢": "Reimu Hakurei",
		"霧雨 魔理沙": "Marisa Kirisame",
		"十六夜 咲夜": "Sakuya Izayoi",
		"フランドール・スカーレット": "Flandre Scarlet",
		"魂魄 妖夢": "Youmu Konpaku",
		"レミリア・スカーレット": "Remilia Scarlet",
		"藤原 妹紅": "Fujiwara no Mokou",
		"古明地 さとり": "Satori Komeiji",
		"アリス・マーガトロイド": "Alice Margatroid",
		"射命丸 文": "Aya Shameimaru",
		"東風谷 早苗": "Sanae Kochiya",
		"比那名居 天子": "Tenshi Hinanawi",
		"秦 こころ": "Hata no Kokoro",
		"西行寺 幽々子": "Yuyuko Saigyouji",
		"鈴仙・優曇華院・イナバ": "Reisen Udongein Inaba",
		"八雲 紫": "Yukari Yakumo",
		"風見 幽香": "Yuuka Kazami",
		"パチュリー・ノーレッジ": "Patchouli Knowledge",
		"多々良 小傘": "Kogasa Tatara",
		"犬走 椛": "Momiji Inubashiri",
		"宇佐見 蓮子": "Renko Usami",
		"紅 美鈴": "Hong Meiling",
		"霊烏路 空": "Utsuho Reiuji",
		"物部 布都": "Mononobe no Futo",
		"聖 白蓮": "Byakuren Hijiri",
		"水橋 パルスィ": "Parsee Mizuhashi",
		"鬼人 正邪": "Seija Kijin",
		"ルーミア": "Rumia",
		"河城 にとり": "Nitori Kawashiro",
		"四季映姫・ヤマザナドゥ": "Eiki Shiki, Yamaxanadu",
		"少名 針妙丸": "Shinmyoumaru Sukuna",
		"洩矢 諏訪子": "Suwako Moriya",
		"茨木 華扇": "Kasen Ibaraki",
		"豊聡耳 神子": "Toyosatomimi no Miko",
		"八雲 藍": "Ran Yakumo",
		"チルノ": "Cirno",
		"封獣 ぬえ": "Nue Houjuu",
		"蓬莱山 輝夜": "Kaguya Houraisan",
		"上白沢 慧音": "Keine Kamishirasawa",
		"永江 衣玖": "Iku Nagae",
		"伊吹 萃香": "Suika Ibuki",
		"鍵山 雛": "Hina Kagiyama",
		"ナズーリン": "Nazrin",
		"火焔猫 燐": "Rin Kaenbyou",
		"今泉 影狼": "Kagerou Imaizumi",
		"宇佐見 菫子": "Sumireko Usami",
		"二ッ岩 マミゾウ": "Mamizou Futatsuiwa",
		"霍 青娥": "Seiga Kaku",
		"ミスティア・ローレライ": "Mystia Lorelei",
		"マエリベリー・ハーン": "Maribel Hearn",
		"小野塚 小町": "Komachi Onozuka",
		"赤蛮奇": "Sekibanki",
		"橙": "Chen",
		"本居 小鈴": "Kosuzu Motoori",
		"八意 永琳": "Eirin Yagokoro",
		"大妖精": "Daiyousei",
		"寅丸 星": "Shou Toramaru",
		"八坂 神奈子": "Kanako Yasaka",
		"姫海棠 はたて": "Hatate Himekaidou",
		"星熊 勇儀": "Yuugi Hoshiguma",
		"因幡 てゐ": "Tewi Inaba",
		"堀川 雷鼓": "Raiko Horikawa",
		"森近 霖之助": "Rinnosuke Morichika",
		"雲居 一輪": "Ichirin Kumoi",
		"村紗 水蜜": "Minamitsu Murasa",
		"ルナサ・プリズムリバー": "Lunasa Prismriver",
		"幽谷 響子": "Kyouko Kasodani",
		"稗田 阿求": "Hieda no Akyuu",
		"小悪魔": "Koakuma",
		"秋 静葉": "Shizuha Aki",
		"岡崎 夢美": "Yumemi Okazaki",
		"秋 穣子": "Minoriko Aki",
		"メディスン・メランコリー": "Medicine Melancholy",
		"リグル・ナイトバグ": "Wriggle Nightbug",
		"黒谷 ヤマメ": "Yamame Kurodani",
		"蘇我 屠自古": "Soga no Tojiko",
		"宮古 芳香": "Yoshika Miyako",
		"神綺": "Shinki",
		"わかさぎ姫": "Wakasagihime",
		"魅魔": "Mima",
		"レティ・ホワイトロック": "Letty Whiterock",
		"綿月 依姫": "Watatsuki no Yorihime",
		"九十九 弁々": "Benben Tsukumo",
		"ルナチャイルド": "Luna Child",
		"スターサファイア": "Star Sapphire",
		"リリカ・プリズムリバー": "Lyrica Prismriver",
		"リリーホワイト": "Lily White",
		"幻月": "Gengetsu",
		"サニーミルク": "Sunny Milk",
		"九十九 八橋": "Yatsuhashi Tsukumo",
		"メルラン・プリズムリバー": "Merlin Prismriver",
		"名無しの本読み妖怪": "Unnamed Book-Reading Youkai",
		"キスメ": "Kisume",
		"綿月 豊姫": "Watatsuki no Toyohime",
		"アリスの人形（上海、蓬莱、大江戸他）": "Alice’s Dolls (Shanghai, Hourai, Ooedo, etc.)",
		"カナ・アナベラル": "Kana Anaberal",
		"夢月": "Mugetsu",
		"夢子": "Yumeko",
		"易者": "Unnamed Jinyou (Fortune Teller)",
		"レイセン": "Rei’sen",
		"雲山": "Unzan",
		"北白河 ちゆり": "Chiyuri Kitashirakawa",
		"サリエル": "Sariel",
		"マイ": "Mai",
		"エリー": "Elly",
		"ユキ": "Yuki",
		"核熱造神ヒソウテンソク": "Thermonuclear Deity Hisou Tensoku",
		"くるみ": "Kurumi",
		"エレン": "Ellen",
		"コンガラ": "Konngara",
		"小兎姫": "Kotohime",
		"魂魄 妖忌": "Youki Konpaku",
		"毛玉": "Kedama",
		"里香": "Rika",
		"レイラ・プリズムリバー": "Layla Prismriver",
		"ルイズ": "Louise",
		"明羅": "Elis",
		"エリス": "Meira",
		"妖精（メイド妖精・ひまわり妖精他）": "Fairy (Maid, Sunflower, etc.)",
		"大ナマズ": "Giant Catfish",
		"ユウゲンマガン": "YuugenMagan",
		"ホフゴブリン": "Hobgoblin",
		"るーこと": "Ruukoto",
		"UFO（赤・青・緑、その他）": "UFOs (red, blue, green, etc.)",
		"オレンジ": "Orange",
		"朝倉 理香子": "Rikako Asakura",
		"万歳楽": "Manzairaku",
		"ツチノコ": "Tsuchinoko",
		"酒虫": "Sake Bug",
		"チュパカブラ": "Tupai",
		"河童（山童含む）": "Kappa (including yamawaro)",
		"都市伝説の怪異（お菊さん、八尺さま他）": "Urban legend entities (Okiku-san, Hasshaku-sama)",
		# "八尺さま": "Hasshaku-sama",
		# "お菊さん": "Okiku-san",
		"ミミちゃん": "Mimi-chan",
		"玄爺": "Genjii",
		"龍（子龍、邪龍他）": "Dragons (Dragon child, Unnamed evil dragon, etc)",
		# "邪龍": "Unnamed Evil Dragon",
		# "子龍": "Dragon Child",
		"岩笠": "Unshou",
		"運松": "Iwakasa",
		"狐（妖怪狐、狐の子他）": "Kitsune (Youkai kitsune, Unnamed fox student, etc)",
		# "狐の子": "Unnamed Fox Student",
		# "妖怪狐": "Youkai Kitsune",
		"華扇の動物（久米、竿打、雷獣、彭祖、人面犬他）": "Kasen's animals (Kume, Kanda, Raijuu, Houso, Jinkenmen, etc)",
		# "大鷲（久米、竿打）": "Steller's Sea Eagles (Kume, Kanda)",
		# "雷獣": "Raijuu",
		# "彭祖": "Houso",
		# "人面犬": "Jinmenken",
		"サラ": "Sara",
		"兎（玉兎、永遠亭の妖怪兎他）": "Rabbits (Moon rabbits, Eientei youkai rabbits, etc)",
		# "月の兎（玉兎）": "Moon Rabbits",
		# "永遠亭の妖怪兎": "Eientei Youkai Rabbits",
		"シンギョク": "SinGyoku",
		"トカゲ": "Unnamed Lizard",
		"キクリ": "Kikuri",
		"命蓮": "Myouren",
		"カラス（地獄鴉、紫・文の使い魔他）": "Crows (Hell ravens, Yukari and Aya's familiars, etc.)",
		"ウワバミ": "Unnamed Snake Youkai",
		"ネッシー号": "Loch Ness Monster",
		"仙台四郎（福の神）": "Shirou Sendai",
		"毘沙門天": "Bishamonten",
		"煙々羅": "Enenra",
		"小鈴の両親": "Kosuzu Motoori's Parents",
		"神降ろしの神霊（天照、伊豆能売他）": "Summoned Gods (Amaterasu, Izunome, etc.)",
		"木花咲耶姫": "Konohana-Sakuyahime",
		"座敷童": "Kutsutsura",
		"沓頬": "Zashiki-warashi",
		"幽霊（怨霊、神霊、化け化け含む）": "Ghosts (including vengeful spirits, divine spirits, bakebake)",
		"狸（化け狸、野鉄砲他）": "Tanuki (Bake-danuki, Noteppou, etc)",
		"月の都の門番": "Moon Capital Gate Guards",
		"天狗（香霖堂の天狗、大天狗他）": "Tengu (Kourindou Tengu, Great Tengu, etc)",
		# "野鉄砲（マミ）": "Noteppou (Mami)",
		"緑の小人": "Little Green Men",
		"大ガマ": "Giant Toad",
		"水江浦島子": "Mizue no Uranoshimako",
		"蓬莱人形ジャケット・レーベルイラストの娘": "Dolls in Pseudo Paradise CD Jacket/Label Girl",
		"清蘭": "Seiran",
		"鈴瑚": "Ringo",
		"ドレミー・スイート": "Doremy Sweet",
		"稀神 サグメ": "Sagume Kishin",
		"クラウンピース": "Clownpiece",
		"純狐": "Junko",
		"ヘカーティア・ラピスラズリ": "Hecatia Lapislazuli",
		"嫦娥": "Chang'e",
	}
}

def jp2en(name):
	if name in touhou["characters"]:
		return touhou["characters"][name]
	return ""

def parse_file(in_file, out_file):
	f = open(in_file, "r", encoding="utf-8")
	s = f.read()

	for name in touhou["characters"]:
		s = s.replace(name, jp2en(name))

	of = open(out_file, "w", encoding="utf-8")
	of.write(s)
	print("->", out_file)

if __name__ == "__main__":
	args = sys.argv[1:]
	if len(args) == 1:
		parse_file(args[0], "out.txt")
	elif len(args) == 2:
		parse_file(args[0], args[1])
	else:
		print("Usage: `python touhou-dict.py input_file [output_file]`")