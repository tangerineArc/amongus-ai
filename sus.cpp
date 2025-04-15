#include<bits/stdc++.h>
using namespace std;


int kill_radius(int bot_x,int bot_y,int time,int W1,int kill_x,int kill_y,int W2,int W3){
        
    if(abs(bot_x-kill_x)+abs(bot_y-kill_y)<=W1*time){
        return W2*W1*time;
    }

    else{
        return W3*W1*time;
    }

}

int following_me(int bot_num1,int bot_num2,vector<vector<int>> v,int W5){
         int cnt=0;
    for(auto it:v[bot_num1]){
        if(it==bot_num2){
            cnt++;
        }
    }

    return cnt*W5;

}

// dqdc

int where_were_you(int bot_num,string given,map<int,pair<int,string>> mp,int W6){
         int bnt1=0;
         int bnt2=0;
       for(auto it:mp){
        if(it.second.first==bot_num){
             if(given==it.second.second){
                  bnt1++;
             }
             bnt2++;
        }
       }

       return (bnt2-bnt1)*W6;
}

int tasks_done_or_not(int bot_num,set<string> s,map<int,pair<int,vector<string>>> mpv,int W7){
        
    int cnt1=0;
    int cnt2=0;

    for(auto it:mpv){
          
        if(it.first==bot_num) continue;

        if(it.second.first==bot_num){
              for(auto ib:it.second.second){
                if(s.count(ib)){
                    cnt1++;
                }
                else{
                    cnt2++;
                }
              }
        }

    }

    return (cnt2-cnt1)*W7;
}

int main(){
     
    //what data i need

    map<pair<int,int>,vector<string>> mpp;    // what tasks first person saw other person do

    map<int,string> ms;    //person vs room they were in

    string kill_pos;

    int kill_x=0;
    int kill_y=0;

    int time=0;

    int bots=0;
   
    map<pair<int,int>,int> mp;
    
    //I will assign some weights to each suss
    //-W1 to person who reported
    //some function for radius in which player could be suss depends on time  let be W2*time
    //people inside W2*time will have W3 suss and rest wont
    //W4,2*W4,3*W4 suss for number of tasks given wrong 
    //W5 SUSS if imposter tells coinciding position and other person denied it
    //i will run a time till time K some K/l tasks should be done and more suss depending upon number of tasks done
    //W6 suss for any bot who says if someone was following them
    
    vector<pair<int,int>> vp;
    
    for(int i=0;i<bots;i++){

        int cnt=0;
           
         for(int j=0;j<bots;j++){
                
            if(j==i) continue;

            //check with respect to bot j for bot i
            
            
         }

    }

    //now ask on a good terminal things like where were you last
    
    //what tasks did you do
}