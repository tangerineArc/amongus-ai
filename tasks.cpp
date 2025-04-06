#include<bits/stdc++.h>
using namespace std;

class BOTS{
    public:
    string ID;
};



int main(){

map<string,vector<pair<int,int>>> ms;

    ms["MED"] = {{2697, 1357}, {2647, 1357}, {2647, 1333}, {2596, 1333}, {2596, 1290}, {2546, 1290}, {2546, 1240}, {2557, 1240}, {2557, 1290}};
    ms["CAMM"] = {{1781, 1192}, {1781, 1189}, {1831, 1189}, {1881, 1189}, {1881, 1138}, {1881, 1133}, {1870, 1133}, {1921, 1133}, {1921, 1183}};
    ms["REAC-UP"] = {{866, 1086}, {866, 1037}, {898, 1037}, {898, 1063}, {848, 1063}, {797, 1063}, {797, 1114}, {847, 1114}, {898, 1114}};
    ms["REAC-DO"] = {{841, 1855}, {816, 1855}, {816, 1804}, {816, 1754}, {867, 1754}, {891, 1754}, {891, 1805}, {841, 1805}, {791, 1805}};
    ms["CAFE-L"] = {{2834, 115}, {2834, 166}, {2784, 166}, {2742, 166}, {2742, 216}, {2692, 216}};
    ms["CAFE-R"] = {{3823, 213}, {3773, 213}, {3773, 181}, {3722, 181}, {3672, 181}, {3672, 131}, {3722, 131}, {3772, 181}};
    ms["ELEC"] = {{2565, 1774}, {2565, 1723}, {2514, 1723}, {2514, 1701}, {2513, 1701}, {2513, 1751}, {2463, 1751}, {2463, 1740}, {2413, 1740}, {2363, 1740}};
    ms["STOR"] = {{3458, 2746}, {3458, 2753}, {3408, 2753}, {3357, 2753}, {3357, 2703}, {3408, 2703}, {3458, 2703}, {3408, 2652}, {3458, 2652}, {3464, 2652}, {3464, 2703}};
    ms["COMM"] = {{4038, 2721}, {4038, 2671}, {3987, 2671}, {3936, 2671}, {3936, 2720}, {3886, 2720}, {3886, 2669}, {3886, 2618}, {3836, 2618}, {3836, 2668}};
    ms["NAVI"] = {{5479, 1298}, {5479, 1293}, {5479, 1343}, {5479, 1393}, {5479, 1432}, {5530, 1432}, {5530, 1397}, {5575, 1397}, {5575, 1447}};
    ms["ENGI-U"] = {{1399, 421}, {1348, 421}, {1298, 421}, {1248, 421}, {1198, 421}, {1198, 471}, {1249, 471}, {1299, 471}, {1350, 471}, {1400, 471}, {1450, 471}};
    ms["ENGI-D"] = {{1174, 2330}, {1124, 2330}, {1124, 2336}, {1174, 2336}, {1174, 2360}, {1224, 2360}, {1224, 2408}, {1275, 2408}, {1275, 2357}, {1275, 2307}, {1224, 2307}, {1224, 2357}};
    ms["OXYG"] = {{4130, 1143}, {4080, 1143}, {4030, 1143}, {4030, 1194}, {3979, 1194}, {3979, 1244}, {3929, 1244}};
    ms["RIGHT-COMM"] = {{4426, 2469}, {4376, 2469}, {4325, 2469}, {4289, 2469}, {4289, 2490}, {4340, 2490}, {4390, 2490}, {4440, 2490}};
    ms["CAFE-ROUND-TABLE"] = {{3448, 681}, {3448, 732}, {3443, 732}, {3443, 782}, {3393, 782}, {3377, 782}, {3377, 832}, {3327, 832}, {3276, 832}, {3276, 789}, {3226, 789}, {3175, 789}, {3175, 760}, {3125, 760}, {3074, 760}, {3074, 710}, {3074, 659}, {3120, 659}, {3120, 609}, {3120, 558}, {3120, 508}, {3171, 508}, {3221, 508}, {3272, 508}, {3322, 508}, {3373, 508}, {3373, 533}, {3423, 533}, {3423, 559}, {3473, 559}, {3523, 559}, {3473, 610}, {3473, 660}, {3473, 711}};

    // return 0;

//MED;
// New Unique Position: (2697, 1357)
// New Unique Position: (2647, 1357)
// New Unique Position: (2647, 1333)
// New Unique Position: (2596, 1333)
// New Unique Position: (2596, 1290)
// New Unique Position: (2546, 1290)
// New Unique Position: (2546, 1240)
// New Unique Position: (2557, 1240)
// New Unique Position: (2557, 1290)



//CAMM
// New Unique Position: (1781, 1192)
// New Unique Position: (1781, 1189)
// New Unique Position: (1831, 1189)
// New Unique Position: (1881, 1189)
// New Unique Position: (1881, 1138)
// New Unique Position: (1881, 1133)
// New Unique Position: (1870, 1133)
// New Unique Position: (1921, 1133)
// New Unique Position: (1921, 1183)



//REAC-UP
// New Unique Position: (866, 1086)
// New Unique Position: (866, 1037)
// New Unique Position: (898, 1037)
// New Unique Position: (898, 1063)
// New Unique Position: (848, 1063)
// New Unique Position: (797, 1063)
// New Unique Position: (797, 1114)
// New Unique Position: (847, 1114)
// New Unique Position: (898, 1114)



//REAC-DO
// New Unique Position: (841, 1855)
// New Unique Position: (816, 1855)
// New Unique Position: (816, 1804)
// New Unique Position: (816, 1754)
// New Unique Position: (867, 1754)
// New Unique Position: (891, 1754)
// New Unique Position: (891, 1805)
// New Unique Position: (841, 1805)
// New Unique Position: (791, 1805)



// CAFE-L
// New Unique Position: (2834, 115)
// New Unique Position: (2834, 166)
// New Unique Position: (2784, 166)
// New Unique Position: (2742, 166)
// New Unique Position: (2742, 216)
// New Unique Position: (2692, 216)



// CAFE-R
// New Unique Position: (3823, 213)
// New Unique Position: (3773, 213)
// New Unique Position: (3773, 181)
// New Unique Position: (3722, 181)
// New Unique Position: (3672, 181)
// New Unique Position: (3672, 131)
// New Unique Position: (3722, 131)
// New Unique Position: (3772, 181)



// ELEC
// New Unique Position: (2565, 1774)
// New Unique Position: (2565, 1723)
// New Unique Position: (2514, 1723)
// New Unique Position: (2514, 1701)
// New Unique Position: (2513, 1701)
// New Unique Position: (2513, 1751)
// New Unique Position: (2463, 1751)
// New Unique Position: (2463, 1740)
// New Unique Position: (2413, 1740)
// New Unique Position: (2363, 1740)



// STOR
// New Unique Position: (3458, 2746)
// New Unique Position: (3458, 2753)
// New Unique Position: (3408, 2753)
// New Unique Position: (3357, 2753)
// New Unique Position: (3357, 2703)
// New Unique Position: (3408, 2703)
// New Unique Position: (3458, 2703)
// New Unique Position: (3408, 2652)
// New Unique Position: (3458, 2652)
// New Unique Position: (3464, 2652)
// New Unique Position: (3464, 2703)



// COMM
// New Unique Position: (4038, 2721)
// New Unique Position: (4038, 2671)
// New Unique Position: (3987, 2671)
// New Unique Position: (3936, 2671)
// New Unique Position: (3936, 2720)
// New Unique Position: (3886, 2720)
// New Unique Position: (3886, 2669)
// New Unique Position: (3886, 2618)
// New Unique Position: (3836, 2618)
// New Unique Position: (3836, 2668)



// NAVI
// New Unique Position: (5479, 1298)
// New Unique Position: (5479, 1293)
// New Unique Position: (5479, 1343)
// New Unique Position: (5479, 1393)
// New Unique Position: (5479, 1432)
// New Unique Position: (5530, 1432)
// New Unique Position: (5530, 1397)
// New Unique Position: (5575, 1397)
// New Unique Position: (5575, 1447)



//ENGI-U
// New Unique Position: (1399, 421)
// New Unique Position: (1348, 421)
// New Unique Position: (1298, 421)
// New Unique Position: (1248, 421)
// New Unique Position: (1198, 421)
// New Unique Position: (1198, 471)
// New Unique Position: (1249, 471)
// New Unique Position: (1299, 471)
// New Unique Position: (1350, 471)
// New Unique Position: (1400, 471)
// New Unique Position: (1450, 471)




//ENGI-D
// New Unique Position: (1174, 2330)
// New Unique Position: (1124, 2330)
// New Unique Position: (1124, 2336)
// New Unique Position: (1174, 2336)
// New Unique Position: (1174, 2360)
// New Unique Position: (1224, 2360)
// New Unique Position: (1224, 2408)
// New Unique Position: (1275, 2408)
// New Unique Position: (1275, 2357)
// New Unique Position: (1275, 2307)
// New Unique Position: (1224, 2307)
// New Unique Position: (1224, 2357)




// OXYG
// New Unique Position: (4130, 1143)
// New Unique Position: (4080, 1143)
// New Unique Position: (4030, 1143)
// New Unique Position: (4030, 1194)
// New Unique Position: (3979, 1194)
// New Unique Position: (3979, 1244)
// New Unique Position: (3929, 1244)




// RIGHT-COMM
// New Unique Position: (4426, 2469)
// New Unique Position: (4376, 2469)
// New Unique Position: (4325, 2469)
// New Unique Position: (4289, 2469)
// New Unique Position: (4289, 2490)
// New Unique Position: (4340, 2490)
// New Unique Position: (4390, 2490)
// New Unique Position: (4440, 2490)




// CAFE-ROUND-TABLE
// New Unique Position: (3448, 681)
// New Unique Position: (3448, 732)
// New Unique Position: (3443, 732)
// New Unique Position: (3443, 782)
// New Unique Position: (3393, 782)
// New Unique Position: (3377, 782)
// New Unique Position: (3377, 832)
// New Unique Position: (3327, 832)
// New Unique Position: (3276, 832)
// New Unique Position: (3276, 789)
// New Unique Position: (3226, 789)
// New Unique Position: (3175, 789)
// New Unique Position: (3175, 760)
// New Unique Position: (3125, 760)
// New Unique Position: (3074, 760)
// New Unique Position: (3074, 710)
// New Unique Position: (3074, 659)
// New Unique Position: (3120, 659)
// New Unique Position: (3120, 609)
// New Unique Position: (3120, 558)
// New Unique Position: (3120, 508)
// New Unique Position: (3171, 508)
// New Unique Position: (3221, 508)
// New Unique Position: (3272, 508)
// New Unique Position: (3322, 508)
// New Unique Position: (3373, 508)
// New Unique Position: (3373, 533)
// New Unique Position: (3423, 533)
// New Unique Position: (3423, 559)
// New Unique Position: (3473, 559)
// New Unique Position: (3523, 559)
// New Unique Position: (3473, 610)
// New Unique Position: (3473, 660)
// New Unique Position: (3473, 711)





}