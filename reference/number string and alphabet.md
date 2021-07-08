

### 프로그래머스 - 숫자 문자열과 영단어 : c++ 프로젝트가 존재하지 않아 임시로 저장

```c++
#include <string>
#include <vector>
#include <iostream>
#include <typeinfo>

using namespace std;

int solution(string s) {
    int answer = 0;

    Alpha alpha[10] = {{0,"zero"},{1,"one"},{2,"two"},{3,"three"},{4,"four"},{5,"five"},{6,"six"},{7,"seven"},{8,"eight"},{9,"nine"}};

    string str = "";
    string result = "";
    for(int i=0; i<s.size(); i++){
        if(static_cast<int>(s[i]) <= 57){
            if(str != ""){
                for(int j=0; j<10; j++){
                    if(str == alpha[j].str){
                        result += to_string(alpha[j].num);    
                    }
                }

            }

            result += s[i];
            str = "";
        }else{
            bool chk = false;
            str += s[i];
            for(int j=0; j<10; j++){
                if(str == alpha[j].str){
                    result += to_string(alpha[j].num);    
                    chk = true;
                    break;
                }
            }
            if(chk){
                str = "";
            }

        }
    }

    cout << result << endl;
    answer = stoi(result);

    return answer;

}
```
