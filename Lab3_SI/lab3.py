import collections


def decrypt(n, ciphertext):
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result


def get_shift_rules(string, lang):

    test = collections.Counter(string.replace(' ', '').replace('.', '').replace(':', '').replace(',', ''))

    test = test.most_common(test.__len__())

    permutations = []
    i = 0

    for letter in test:

        original_pos = key.index(letter[0])
        permutated_pos = key.index(lang[i])
        permutation = abs(original_pos - permutated_pos)

        i += 1
        permutations.append(permutation)

    return permutations


def spell_checker(string):

    words = string.split()

    for word in words:
        if word in english_words:
            print (string)


def solve(string, lang):

    rules = get_shift_rules(string, lang)

    for rule in rules:
        result = decrypt(rule, string)
        words = result.split()
        for word in words:
            if word in english_words:
                print (result)

                return



string1 = "WKHSWEC: WI XKWO SC WKHSWEC NOMSWEC WOBSNSEC, MYWWKXNOB YP DRO KBWSOC YP DRO XYBDR, QOXOBKV YP DRO POVSH " \
          "VOQSYXC, VYIKV COBFKXD DY DRO DBEO OWZOBYB, WKBMEC KEBOVSEC. PKDROB DY K WEBNOBON CYX, RECLKXN DY K WEBNOBON " \
          "GSPO. KXN S GSVV RKFO WI FOXQOKXMO, SX DRSC VSPO YB DRO XOHD."
string2 = 'XOXKR IETG BL MH UX VHGLBWXKXW, XOXKR XQIXWBXGM MKBXW TGW XOXKR FXMAHW MTDXG UXYHKX FTMMXKL TKX UKHNZAM MH ' \
          'MABL ETLM XQMKXFBMR. ZHHW HYYBVXKL WXVEBGX ZXGXKTE XGZTZXFXGML PAXKX MAX HWWL TKX MHH ZKXTM, TGW IKXYXK MAX' \
          ' XFIEHRFXGM HY LMKTMTZXF TGW YBGXLLX MH WXLMKHR MAX XGXFR TL FNVA TL IHLLBUEX PBMAHNM XQIHLBGZ MAXBK HPG YHKVXL.'
string3 = 'RD QTAJ KTW YMJ WTRFS JRUNWJ NX ZSIJSNFGQD LWJFYJW YMFS KTW RDXJQK. YMJ LWJFYJXY JRUNWJ JAJW YT MFAJ JCNXYJI.' \
          ' N UQJILJ RD JYJWSFQ XJWANYZIJ FSI N FR KTWJAJW GTZSI YT XJWAJ NY, NS QNKJ FSI NS IJFYM. YMJD MFAJ RJWJQD LNAJS ' \
          'ZX: WTFIX, HJSYWFQ MJFYNSL, HTSHWJYJ, YMJ HFQJSIFW, FSI KQZXMNSL YTNQJYX FSI XJBJWX.'
deadline = 'AB ZNRL MAX WXTWEBGX YHK MABL ETUHKTMHKR BL MAX MPXGMBXMA HY WXVXFUXK B PHNEW EBDX MH PBLA RHN ZHHW ENVD ' \
           'PBMA BM TGW ATOX T GBVX EBYX'



key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_frequency_english = 'ETAOINSRHLDCUMFPGWYBVKXJQZ'
#letter_frequency_french = 'EASTIRNULODMCPEVHGFBQJAXEEZYKOUWIAUU'


english_words = ['IS', 'THE', 'AM', 'I', 'ARE', 'YOU', 'TO', 'MY', 'BE', 'AND', 'AS', 'IT', 'IN']


solve(string1, letter_frequency_english)
solve(string2, letter_frequency_english)
solve(string3, letter_frequency_english)
