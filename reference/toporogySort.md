### 위상정렬 Toporogy Sort

> 순서가 정해져있는 작업을 차례로 수행해야 할 때 그 순서를 결정해주기 위해 사용

### 구현방법

> 1. 진입차수가 0인 정점을 큐에 삽입
> 2. 큐에서 원소를 꺼내 연결된 모든 간선을 제거
> 3. 간선 제거 이후에 진입차수가 0이된 정점을 큐에 삽입
> 4. 큐가 빌때까지 2~3번 과정을 반복
>
> - 모든 원소를 방문하기 전에 큐가 빈다면 싸이클이 존재하는 것이고, 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과이다





### 문제

> N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.
>
> 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

### 입력

> 첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다. M은 키를 비교한 회수이다. 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.
>
> 학생들의 번호는 1번부터 N번이다.

### 출력

> 첫째 줄에 학생들을 키 순서대로 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.



### 참고소스

```python
# [TopologySort] 줄 세우기 - 백준 2252

import sys
from collections import deque

N,M = list(map(int,sys.stdin.readline().split()))

nodeLine = [0] * (N+1)
node = [[] for _ in range(N+1)]

for i in range(M):
    a,b = list(map(int,sys.stdin.readline().split()))
    node[a].append(b)
    nodeLine[b] += 1



def topologySort(node,nodeLine):

    q = deque()
    result = []

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,N+1):
        if(nodeLine[i] == 0):
            result.append(i)
            q.append(i)

    # 위상 정렬이 완전히 수행되려면 정확히 N개의 노드를 방문, 중간에 q가 null 이 되면 싸이클이 존재한는 것이다.
    for i in range(1,N+1):
        x = q.popleft()
        if(len(node[x]) > 0):
            for j in node[x]:
                nodeLine[j] -= 1
                if(nodeLine[j] == 0):
                    result.append(j)
                    q.append(j)

    return result

result = topologySort(node,nodeLine)

for i in result:
    print(i,end=' ')
```

### 예제입력

> ```
> 4 2
> 4 2
> 3 1
> ```

### 소스결과

> ```
> 4 2 3 1
> ```

