#include <iostream>
#include <vector>
#include <utility>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cfloat>
#include <iomanip>
using namespace std;

const int maxN = 520;
int n;
float a, b, c;
pair<float, float> start, finish;
vector<pair<pair<float, float>, float>> trees;
vector<pair<float, int>> graph[maxN];
float dist[maxN];
bool visited[maxN], pushed[maxN];
priority_queue<pair<float, int>, vector<pair<float, int>>, greater<pair<float, int>>> priorityQueue;
void dijkstras()
{
    int a = 0, tempVert;
    float tempWeight;
    for (int i = 0; i < n + 2; i++)
    {
        dist[i] = FLT_MAX;
    }
    dist[a] = 0;
    priorityQueue.push(pair<float, int>(dist[a], a));
    visited[a] = true;
    while (!priorityQueue.empty())
    {
        a = priorityQueue.top().second;
        priorityQueue.pop();
        visited[a] = true;
        for (int i = 0; i < graph[a].size(); i++)
        {
            tempVert = graph[a][i].second;
            tempWeight = graph[a][i].first;
            if (dist[tempVert] > dist[a] + tempWeight && dist[a] != FLT_MAX)
            {
                dist[tempVert] = dist[a] + tempWeight;
                if (!visited[tempVert])
                {
                    priorityQueue.push(pair<float, int>(tempWeight, tempVert));
                }
            }
        }
    }
}
float findDist(pair<float, float> a, pair<float, float> b)
{
    return sqrt((a.first - b.first) * (a.first - b.first) + (a.second - b.second) * (a.second - b.second));
}
int main()
{
    cin >> start.first >> start.second >> finish.first >> finish.second;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> a >> b >> c;
        trees.push_back(pair<pair<float, float>, float>(pair<float, float>(a, b), c));
    }
    graph[0].push_back(pair<float, int>(findDist(start, finish), 1));
    graph[1].push_back(pair<float, int>(findDist(start, finish), 0));
    for (int i = 0; i < n; i++)
    {
        graph[0].push_back(pair<float, int>(max(findDist(start, trees[i].first) - trees[i].second, (float)0), i + 2));
        graph[i + 2].push_back(pair<float, int>(max(findDist(start, trees[i].first) - trees[i].second, (float)0), 0));
        graph[1].push_back(pair<float,int>(max(findDist(finish,trees[i].first)-trees[i].second,(float)0), i + 2));
        graph[i + 2].push_back(pair<float, int>(max(findDist(finish, trees[i].first) - trees[i].second, (float)0), 1));
        for (int j = i + 1; j < n; j++)
        {
            graph[i + 2].push_back(pair<float, int>(max(findDist(trees[i].first, trees[j].first) - trees[i].second - trees[j].second, (float)0), j + 2));
            graph[j + 2].push_back(pair<float, int>(max(findDist(trees[i].first, trees[j].first) - trees[i].second - trees[j].second, (float)0), i + 2));
        }
    }
    dijkstras();
    cout << setprecision(100000) << dist[1];
}