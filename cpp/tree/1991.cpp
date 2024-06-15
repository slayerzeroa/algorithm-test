#include <iostream>
#include <vector>
#include <string>
#define MAX 26

using namespace std;

struct node{
    char left;
    char right;
};

void preOrder(char node);
void inOrder(char node);
void postOrder(char node);

vector<node> tree(MAX);

int main() {
    char root;
    char left;
    char right;
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> root >> left >> right;
        tree[root].left = left;
        tree[root].right = right;
    }
    preOrder('A');
    cout << endl;
    inOrder('A');
    cout << endl;
    postOrder('A');
}


void preOrder(char node){
    if (node == '.') return;
    cout << node;
    preOrder(tree[node].left);
    preOrder(tree[node].right);
}

void inOrder(char node){
    if (node == '.') return;
    inOrder(tree[node].left);
    cout << node;
    inOrder(tree[node].right);
}

void postOrder(char node){
    if (node == '.') return;
    postOrder(tree[node].left);
    postOrder(tree[node].right);
    cout << node;
}