#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
#include <ctime>

using namespace std;

bool compare(string a, string b){
        return a<b;
}

vector<string> lst;

vector<string> DFS(vector<vector<string>> tickets,string before,string go){
    //int i = 0
    lst.push_back(go.c_str());
    while(tickets.size()!=0){
        vector<string> q;
        //find queue lst in tickets & remove used ticket 
        for (int i = 0; i < tickets.size(); i++) {
            if(before == tickets[i][0].c_str() and go==tickets[i][1].c_str()){
                //printf("remove tiket: %s %s\n",before.c_str(),go.c_str());
                tickets.erase(tickets.begin()+i);
            }
            if(go == tickets[i][0].c_str()){
                //printf("%s %s\n",tickets[i][0].c_str(),tickets[i][1].c_str());
                q.push_back(tickets[i][1].c_str());
            }
        }
        //queue 알파벳 순으로 정렬
        sort(q.begin(),q.end(),compare);
        
	    while(!q.empty()) {
            string dis = q.front();
            //printf("dis: %s \n",dis.c_str());
            //lst.push_back(dis.c_str());
            DFS(tickets,go,dis);
	        q.erase(q.begin()+1);
	    }
    }
    return lst;
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    answer = DFS(tickets,"FIRST","ICN");
    return answer;
}
