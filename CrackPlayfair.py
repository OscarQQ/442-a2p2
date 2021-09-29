import random
import ngram_score as ns
fitness = ns.ngram_score('english_quadgrams.txt')
Alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]


def initializeKey():
    random_key = ''.join(random.sample(Alpha, len(Alpha)))
    key = matrix(5, 5, 0)
    k = 0
    for i in range(0, 5):
        for j in range(0, 5):
            key[i][j] = random_key[k]
            k += 1
    return key


def swapTwoLetter(key):
    flag = 0
    while flag != 1:
        x1 = random.randint(0, 4)
        y1 = random.randint(0, 4)
        x2 = random.randint(0, 4)
        y2 = random.randint(0, 4)
        if x1 != x2 | y1 != y2:
            flag = 1
    temp = key[x1][y1]
    key[x1][y1] = key[x2][y2]
    key[x2][y2] = temp

def locationOfLetter(char, key):
    location = list()
    for i, j in enumerate(key):
        for k, l in enumerate(j):
            if char == l:
                location.append(i)
                location.append(k)
                return location


def crack():
    key = initializeKey()
    max_score = -100000000000
    count = 1
    text = "QEXBCESKYEVOBGENSIVCFEONELSRCHSEQEFRVEURZCOZELUAIRFSRENQSBBOCTTEWTDLXCWTECFRFSMTTNTSAEWTBHNQTRREOVXAXBOWGTEZEDNOSRMQSRHXOZHXXBLNSBUVEVNGXBLSSRHXUSHGVNOLZCBOIBCWVLBWGKWRCPOLBPBGSBBOWTCGEDISQKUIWTQIHTTSAEUWREQALEEQTRTWGKOLBPBGQIBHTPEPTQPNZOCYNOAEOLBPBGSBNQCVFSAZECBWGKXBHXWTUSTPPZXSBEGTCGSIDMLESBKQXUCSAEWTTLROOZTGODOLBPBGQIBHTPPGSRECKMELGRFSMSZFEDWTFELDBGSBNQLOLDRLTZRSELOVDZKABVKQMSOVXHKMUIWTQIXBLSSRHXWTQBOLBPBGWTUSTPTMTSLBZDRSOUVCFSUSTPEPLTTEUAAWTSBQTPTGDTHCXBRSTVLDWKCATZLRVEKGWRAELQQFCWWNBHEHONRWSFONLEQENTCVQLVOTUTRRSOLBPBGDZVFSCKMIELDBGVCXSTPEZGCOZCENTNRTPOMLEXBRETRLBEVKSMSXBRWLTKQRSUSXBXBLSSRREUWQINCSWTCBOWTCGEDELXBLSSRHXXBVEERVELDSBMNQBTWGKREECXEWTXFRWREOCCVLYOVXAXBCTQCBSELKELRSIWRBOWXCYAZXBONTVEVOLBPBGSBMQTGKESKASVEWKNQSHOLBPBGELUAARIWFXFSWROLBPBGXBHXNTVCSRXBCEWXEDRNSIHTGTTLVRIUSROLBPBGQEIURSOCSBMQTLUSMSWTOLZCNQTIFECTHDTSXELQGHCWVLKSOBLEUAIRSFAEXBCYAZEHSIXBHXLYBHMNHQTFFUNOBETIZIBXEDIUSRSBNYSIKHSESKIZXMHCUWREWTEXSCBOLQEDTSSRFELDBGXBTWTSEHSIQESKECEWCEBHCAEASKSLBYQIUWQINCSWOLBPBGSBBYCOSRXLTHFCEXLNMTSKZPHOTQGRLEERSXRSXBONTVEVOVXAXBREGTEYOLBPBGIYSCOXCQOCTINLVFLDXBTNGTTLVRIUSROLBPBGSBBOWTWRNRSRXBRNEVNQACGRCDCSGBLYOLBPBGXBLSSRHXSBBORSFSMTONLEUWTQSRDVKFLDBGSBNYWZOVDVWITRCNNLSBBOWTCGEDSBWNRSONOLBPBGQSBGOLHSVNOZCGEDOLBPBGIXXSQKCVORRSHOUAMSOVCATINLELDVHCTDLSXBHXDVZIQFLNCOCYXSSLOLBPBGQEXBHXSKSRGTACUQBGHDCOLDCEWTCUMSCVNTSIEAOLBPBGSINLKEGTPLONLEUWWQYTZCKQAQRODVKFCYXSSLNOBGKMONLYOVXTCOIHWRCVGTEZGUSXNQDVHISRXBLSSRHXRWEOLDBGSBBQTLERBHROVLNRXELQXSBEDZSRIYRWEOLDBGSBWNRSONXBCTQCKMLEXBTNGTTLVRIUSRKHSEONIURSOCOZVCXSCANLOLBPBGSBBOWTQVUFRWSQKOLDBGNXSKZLLRVECVXBHXXBRNUFNCNYACTUQINOQBOLBPBGSBBOBHLBLDRECAUSTPPZQFOWCYOLWFSAONLEKHXHGEEDASAEWTUSEOZTQFRWOLBPBGDVZKWIEXLNSQBSOLHSVNOVXAXBCTQCENSISBSPHQXAXBQIGRTRCOUTLDBGKHEOCYOMISWDLEUAMSSKSRGPUOLDBGSBNYUATCWTAETVVOIQTCBEOZASUGMSHXXBTNGTTLVRIUSRACNTTINLQEIKFSCYGEZWLEXBHXWTCHSEONXHGCSBNVWIWTKVVEBLWTVELDOVXBRNSIZPQBELIUKMUAIRFSRENQHSACSKIPEVUAKLLDBGSBBOLTBOWTDLXUQIECFRFSMTCSBERSFQRNUSXBXBRNGUSXBVOVEHBHEABHTPEZONEDEYSINCBVOVVEXBWQQBOZOVXAXBRSCSQEMEDVERXBSKSZCOSBOVOLBPBGSRCHSEONXBCTQCKELDBGSBBOBHCAAELQLELEWTTGKMCVXBRNSKCURWOLBPBGWRCNCYXAXBRNUFNCNYACTUOLBPBGSBBVNOAEVEZWRSOVXTHCIWXRVLWRNRTIBRDEEASQBOWTAQPEOVXAXBREQIBHTPEMORRSBHROOLWFSACOLDBGNOOTSXONXBCTQCKMLESBKQAWGTEMORRSBHRONXSQEWOLBPBGQBNOBOWTIESXCOVEYNLESBKQAWGTEMORRSBHROHBTSXEOLBPBGGRCDCEWTCAENTVVOBGKMLESBKQAWGTEMORRSWRTSWKECBGKMWKOTTWREVWOLBPBGISQKOVVEXBUOLDBGNTAQBRKSMSELEFDOLENTTISRIKTOFSONXBLSSRREAQPEOVXAXBCETSSWUSTPCPGTTLDWCYPSSRREIQCMQLNESBNQVLCAOBLEQEOVVEXBDOFSONWTSRWOISKMISQKOLBPBGQIZFVLWRNRKZAEEXUQXTHCQSNGWFCSOVDEEHSBXAELCUTPTGDWDTODOLBPBGORREELWRTSWKECBGASSK"
    while 1:
        plaintext = decipher(text, key)
        score = fitness.score(plaintext)
        if score > max_score:
            max_score = score
            print(f'On iteration {count}, score is {score}')
            print(plaintext)
        count += 1
        swapTwoLetter(key)

def decipher(text, key):
    i = 0
    plaintext = ''
    while i < len(text):
        l1 = locationOfLetter(text[i], key)
        l2 = locationOfLetter(text[i + 1], key)
        if l1[0] == l2[0]:
            plaintext += key[l1[0]][(l1[1] - 1) % 5] + key[l2[0]][(l2[1] - 1) % 5]
        elif l1[1] == l2[1]:
            plaintext += key[(l1[0] - 1) % 5][l1[1]] + key[(l2[0] - 1) % 5][l2[1]]
        else:
            plaintext += key[l1[0]][l2[1]] + key[l2[0]][l1[1]]
        i = i + 2
    return plaintext

crack()
