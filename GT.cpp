#include <iostream>
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
int main(void)
{
    ifstream fin("input.txt");
    string time_stamp, process_ID, process_command_name, status;
    string IP_type, protocol_name, Internet_address, temp;
    int cnt = 0, len = 0;
    while(fin >> temp) {
        cnt++;
        if(cnt > 22)
            break;
        len = temp.length();
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
