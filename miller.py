#!/usr/bin/python3
import random
import argparse
import sys

SPRIMES = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,
103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,
199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,
313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,
433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,
563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,
673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,
811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,
941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,
1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,
1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,
1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,
1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,
1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,
1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,
1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,
1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,
1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,
2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,
2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,
2297,2309,2311,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,
2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,
2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,2633,2647,2657,2659,2663]

MPRIMES = [299417,299419,299447,299471,299473,299477,299479,299501,299513,299521,
299527,299539,299567,299569,299603,299617,299623,299653,299671,299681,
299683,299699,299701,299711,299723,299731,299743,299749,299771,299777,
299807,299843,299857,299861,299881,299891,299903,299909,299933,299941,
299951,299969,299977,299983,299993,300007,300017,300023,300043,300073,
300089,300109,300119,300137,300149,300151,300163,300187,300191,300193,
300221,300229,300233,300239,300247,300277,300299,300301,300317,300319,
300323,300331,300343,300347,300367,300397,300413,300427,300431,300439,
300463,300481,300491,300493,300497,300499,300511,300557,300569,300581,
300583,300589,300593,300623,300631,300647,300649,300661,300667,300673,
300683,300691,300719,300721,300733,300739,300743,300749,300757,300761,
300779,300787,300799,300809,300821,300823,300851,300857,300869,300877,
300889,300893,300929,300931,300953,300961,300967,300973,300977,300997,
301013,301027,301039,301051,301057,301073,301079,301123,301127,301141,
301153,301159,301177,301181,301183,301211,301219,301237,301241,301243,
301247,301267,301303,301319,301331,301333,301349,301361,301363,301381,
301403,301409,301423,301429,301447,301459,301463,301471,301487,301489,
301493,301501,301531,301577,301579,301583,301591,301601,301619,301627,
301643,301649,301657,301669,301673,301681,301703,301711,301747,301751,
301753,301759,301789,301793,301813,301831,301841,301843,301867,301877]

LPRIMES = [996103,996109,996119,996143,996157,996161,996167,996169,996173,996187,
996197,996209,996211,996253,996257,996263,996271,996293,996301,996311,
996323,996329,996361,996367,996403,996407,996409,996431,996461,996487,
996511,996529,996539,996551,996563,996571,996599,996601,996617,996629,
996631,996637,996647,996649,996689,996703,996739,996763,996781,996803,
996811,996841,996847,996857,996859,996871,996881,996883,996887,996899,
996953,996967,996973,996979,997001,997013,997019,997021,997037,997043,
997057,997069,997081,997091,997097,997099,997103,997109,997111,997121,
997123,997141,997147,997151,997153,997163,997201,997207,997219,997247,
997259,997267,997273,997279,997307,997309,997319,997327,997333,997343,
997357,997369,997379,997391,997427,997433,997439,997453,997463,997511,
997541,997547,997553,997573,997583,997589,997597,997609,997627,997637,
997649,997651,997663,997681,997693,997699,997727,997739,997741,997751,
997769,997783,997793,997807,997811,997813,997877,997879,997889,997891,
997897,997933,997949,997961,997963,997973,997991,998009,998017,998027,
998029,998069,998071,998077,998083,998111,998117,998147,998161,998167,
998197,998201,998213,998219,998237,998243,998273,998281,998287,998311,
998329,998353,998377,998381,998399,998411,998419,998423,998429,998443,
998471,998497,998513,998527,998537,998539,998551,998561,998617,998623,
998629,998633,998651,998653,998681,998687,998689,998717,998737,998743,
998749,998759,998779,998813,998819,998831,998839,998843,998857,998861,
998897,998909,998917,998927,998941,998947,998951,998957,998969,998983,
998989,999007,999023,999029,999043,999049,999067,999083,999091,999101,
999133,999149,999169,999181,999199,999217,999221,999233,999239,999269,
999287,999307,999329,999331,999359,999371,999377,999389,999431,999433,
999437,999451,999491,999499,999521,999529,999541,999553,999563,999599,
999611,999613,999623,999631,999653,999667,999671,999683,999721,999727,
999749,999763,999769,999773,999809,999853,999863,999883,999907,999917,
999931,999953,999959,999961,999979,999983]


PRIME200 = [58021664585639791181184025950440248398226136069516938232493687505822471836536824298822733710342250697739996825938232641940670857624514103125986134050997697160127301547995788468137887651823707102007839,
            29072553456409183479268752003825253455672839222789445223234915115682921921621182714164684048719891059149763352939888629001652768286998932224000980861127751097886364432307005283784155195197202827350411,
            41184172451867371867686906412307989908388177848827102865167949679167771021417488428983978626721272105583120243720400358313998904049755363682307706550788498535402989510396285940007396534556364659633739,
            54661163828798316406139641599131347203445399912295442826728168170210404446004717881354193865401223990331513412680314853190460368937597393179445867548835085746203514200061810259071519181681661892618329,
            71611195866368241734230315014260885890178941731009368469658803702463720956633120935294831101757574996161931982864195542669330457046568876289241536680683601749507786059442920003278263334056542642264651,
            28591045597720075832628274729885724490653298360003309382769144463123258670807750560985604954275365591715208615509779345682419533206637382048824349415329839450792353652240682445321955199147316594996133,
            49790921912819110019003521637763748399072771256062128988437189616228355821145834783451215869998723492323628198577054239101181556609916127864608488018093426129641387774385490891035446702272744866010729,
            15474811206486587193258690501682404626361341756658894201908294153626080782693777003022566996735796983239343580281979005677758015801189957392350213806122307985157041153484138150252828152419133170303749,
            12654646219963267405298825104551142450213038420566798208417393291567314379831789259173233506811083774527183953999862675239292185131178671317061020444490733287588383918793095608410078925861028249824377,
            40992408416096028179761232532587525402909285099086220133403920525409552083528606215439915948260875718893797824735118621138192569490840098061133066650255608065609253901288801302035441884878187944219033]

def millersTest(n):
    # Returns True if num is a prime number.
#    n = num - 1
    t = n - 1
    s = 0
    while t % 2 == 0:
        # keep halving t while it is even (and use s
        # to count how many times we halve t)
        t = t // 2
        s += 1
    b = random.randrange(2, n)
    if pow(b, t, n) == 1:
        return True
    p = t
    for i in range(s):
        if pow(b, p, n) == n - 1:
            return True
        p *= 2
    return False


def isPrimeMiller(n):
    testTimes = 20
    for i in range(testTimes):
        ok = millersTest(n)
        if not ok:
            return False
    return True


def test():
    # test a few small numbers
    print("testing small numbers")
    testLoop(SPRIMES)
    print("\ntesting medium numbers")
    testLoop(MPRIMES)
    print("\ntesting larger numbers")
    testLoop(LPRIMES)
    print("\ntesting 200 digit numbers")
    testLoop(PRIME200)


def testLoop(nums):
    for i in range(len(nums) - 1):
        # test if prime
        if not isPrimeMiller(nums[i]):
            print(nums[i], "failed")
        # test if composite is prime
        comp = nums[i] * nums[i + 1]
        if isPrimeMiller(comp):
            print(comp, "failed")
        # if test pass print dot
        else:
            print('.', end = '')


def main():
    #Get Command Line Arguments
    parser = argparse.ArgumentParser(description='Enter a number')
    parser.add_argument('n', type=int, help='Any positive integer greater than 1')
    parser.add_argument('-t', '--test', action='store_true',
    help="runs test function")
    args = parser.parse_args()

    if args.test:
        test()
        sys.exit()

    # Check if number is greater than 1
    if args.n <= 1:
        parser.error("Please enter a number greater than 1")

    # edge case to check for 2
    if args.n == 2:
        print("true")
    # bailout if number is even
    elif args.n % 2 == 0:
        print("false")
    elif isPrimeMiller(args.n):
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    main()
    #test()
