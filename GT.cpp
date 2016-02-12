#include <iostream>
#include <regex.h>
#include <sys/types.h>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <string>
using namespace std;
typedef struct _Quintet {
    string SrcIp;
    string SrcPort;
    string DstIP;
    string DstPort;
    string Stat;
} Quintet;

int re(string input, Quintet &quintet)
{
    int status;
    regex_t reg;
    regmatch_t pmatch[5];
    const char *pattern = "(.*):(.*)::(.*):(.*)";
    const size_t nmatch = 5;
    regcomp (&reg, pattern, REG_EXTENDED);
    status = regexec(&reg, input.c_str(), nmatch, pmatch, REG_NOTEOL);
    cout<<"In fun"<<endl;
    if(status == REG_NOMATCH) {
        cout<<"NO MATCH"<<endl;
        return 0;
    } else if(status == 0) {
        for(int x = 0; x < nmatch && pmatch[x].rm_so != -1; ++x) {
            cout<<" x "<<x<<" is "<<input.substr(pmatch[x].rm_so, pmatch[x].rm_eo)<<endl;
        }
    }
    regfree(&reg);
    return 1;
}

int main(void)
{
    ifstream fin("input.txt");
    string time_stamp, process_ID, process_command_name, status;
    string IP_type, protocol_name, Internet_address, temp;
    int cnt = 0, len = 0;
    while(fin >> temp) {//if have space, use getline
        cnt++;
        if(cnt > 22)
            break;
        len = temp.length();
        Quintet quintet;
        switch(temp[0]) {
            case 'c':
                process_command_name = temp.erase(0, 1);
                cout<<"process_command_name "<<process_command_name<<endl;
                break;
            case 't':
                IP_type = temp.erase(0, 1);
                cout<<"IP_type "<<IP_type<<endl;
                break;
            case 'p':
                process_ID = temp.erase(0, 1);
                cout<<"process_ID "<<process_ID<<endl;
                break;
            case 'P':
                protocol_name = temp.erase(0, 1);
                cout<<"protocol_name "<<protocol_name<<endl;
                break;
            case 'n':
                Internet_address = temp.erase(0, 1);
                cout<<"Internet_address "<<Internet_address<<endl;
                re(Internet_address, quintet);
                break;
            case 'f':
                status = temp.erase(0, 1);
                cout<<"status "<<status<<endl;
                break;
            default:
                time_stamp = temp;
                cout<<"time_stamp "<<time_stamp<<endl;
                break;
        }
    }
    return 0;
}
