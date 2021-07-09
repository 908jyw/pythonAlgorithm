#include <string>

#include <vector>

#include <iostream> // cout << "abc" << endl;

#include <queue>

#include <algorithm>

using namespace std;



priority_queue<int,vector<int>,greater<int>> pq (v.begin(),v.end());  // int형 우선순위 큐 선언과 함께 벡터 v값을 삽입



// 구조체를 이용한 우선순위 큐 사용법

struct man {

​      int age;

​      int h, w;

};

struct compare {

​      bool operator()(man m1, man m2) {

​      return m1.age < m2.age;

}

priority_queue<man, vector<man>, compare> mq; // 내가 정의한 비교구문으로 뽑고 싶을때

priority_queue<int, vector<int>, greater<int>> g_pq; //작은것을 뽑고 싶을때

priority_queue<int, vector<int>, less<int>> l_pq; // 큰것을 뽑고 싶을때



sort(arrN.begin(),arrN.end()); // arrN 오름차순 정렬

sort(arrN.begin(),arrN.end(), less<int>());  // arrN 오름차순 정렬

sort(arrN.begin(),arrN.end(), greater<int>());      // arrN 내림차순 정렬



std::vector<int> A;

std::vector<int> B;

std::vector<int> AB;



AB.reserve( A.size() + B.size() ); // preallocate memory

AB.insert( AB.end(), A.begin(), A.end() );

AB.insert( AB.end(), B.begin(), B.end() );



 

// iterator 사용법

set<int>::iterator iter;

bool result;

for(iter = s.begin(); iter != s.end(); iter++){

​      cout << *iter << " " ;

​      result = isPrime(*iter);

​      if(result){

​           answer += 1;

​      }

}  



// 3진법 만들기

string change(int n){  

  char ch[3] = {'0','1','2'};

  string str = "";

  while(n/3>0){

​    str = ch[n%3] + str;

​    n /= 3;

  }

  str = ch[n%3] + str;

  return str;

}



// newStr = 삼진법으로 표현된 수, 3 = 3진법을 나타냄

answer = stoi(newStr,NULL,3); // 결과는 3진법으로 표현된 수를 10진법으로 바꿔서 보여줌



// 아스키코드 만들기

cout << static_cast<int>('a') << endl;



stoi() // 스트링 값을 숫자로 변환

to_string() // 숫자를 스트링값으로 변환

char ch = '1';

ch - '0' -> 인티저 1이 나옴

(int)ch -> 아스키코드 값이 나옴 



벡터 기본 함수



iterator(반복자)

begin(): beginning iterator를 반환

end(): end iterator를 반환



추가 및 삭제

push_back(element): 벡터 제일 뒤에 원소 추가

pop_back(): 벡터 제일 뒤에 원소 삭제



조회

[i]: i번째 원소를 반환

at(i): i번째 원소를 반환

front(): 첫번째 원소를 반환

back(): 마지막 원소를 반환



기타

empty(): 벡터가 비어있으면 true 아니면 false를 반환

size(): 벡터 원소들의 수를 반환



큐 기본 함수

추가 및 삭제

push(element): 큐에 원소를 추가(뒤에)

pop(): 큐에 있는 원소를 삭제(앞에)



조회

front(): 큐 제일 앞에 있는 원소를 반환

back(): 큐 제일 뒤에 있는 원소를 반환



기타

empty(): 큐가 비어있으면 true 아니면 false를 반환

size(): 큐 사이즈를 반환