import re
####################################################
# .	任意の1文字	a.c	abc, acc, aac                  #
# ^	行の先頭	^abc	abcdef                     #
# $	行の末尾	abc$	defabc                     #
# *	0回以上の繰り返し	ab*	a, ab, abb, abbb       #
# +	1回以上の繰り返し	ab+	ab, abb, abbb          #
# ?	0回または1回	ab?	a, ab                      #
# {m}	m回の繰り返し	a{3}	aaa                #
# {m,n}	m〜n回の繰り返し	a{2, 4}	aa, aaa, aaaa  #
# [★]	★のどれか1文字	[a-c]	a, b, c          #
# ★|★	★のどれか	a|b	a, b                　  #
####################################################

# 郵便番号 「数字3桁-数字4桁」を表す正規表現オブジェクトの生成
value = "020-0003"
reg = re.compile(r"^d{3}-¥d{4}$")

if not(reg.match(value)):
    print("郵便番号の形式ddd-ddddにマッチしていません。")
else:
    print("マッチしています")