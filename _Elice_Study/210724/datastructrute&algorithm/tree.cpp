#include <stdio.h>
#include <stdlib.h>
#include <queue>
using namespace std;

typedef struct _node {

	int data;
	struct _node* lChild;
	struct _node* rChild;

}Node;

Node* AllocNode(int data) {

	Node* n = (Node*)malloc(sizeof(Node));
	n->data = data;
	n->lChild = n->rChild = NULL;

	return n;
}

void Inorder(Node* root) {

	if (root == NULL)
		return;
	Inorder(root->lChild);
	printf("%d ", root->data);
	Inorder(root->rChild);

}

void Preorder(Node* root) {
	if (root == NULL)
		return;
	printf("%d ", root->data);
	Preorder(root->lChild);
	Preorder(root->rChild);
}

void Postorder(Node* root) {
	if (root == NULL)
		return;
	Postorder(root->lChild);
	Postorder(root->rChild);
	printf("%d ", root->data);

}

void Levelorder(Node* root) {
	if (root == NULL)
		return;

	queue<Node*> q;
	q.push(root);

	while (!q.empty()) {
		Node* front = q.front();
		q.pop();
		printf("%d ", front->data);

		if (front->lChild != NULL)
			q.push(front->lChild);
		if (front->rChild != NULL)
			q.push(front->rChild);

	}
}

Node* AddNode(Node* root, int data) {
	if (root == NULL)
		return AllocNode(data);

	if (data < root->data)
		root->lChild = AddNode(root->lChild, data);
	else
		root->rChild = AddNode(root->rChild, data);

	return root;
}

void FreeNode(Node* root) {
	if (root == NULL)
		return;
	FreeNode(root->lChild);
	FreeNode(root->rChild);
	
	free(root);
}

Node* SearchNode(Node* root, int data) {

	if(root == NULL)
		return NULL;

	if (data < root->data)
		return SearchNode(root->lChild, data);
	else if (data > root->data)
		return SearchNode(root->rChild, data);
	else
		return root;
}

int main() {

	Node* root = NULL;

	root = AddNode(root, 50);
	root = AddNode(root, 30);
	root = AddNode(root, 70);
	root = AddNode(root, 10);
	root = AddNode(root, 40); 
	root = AddNode(root, 60);
	root = AddNode(root, 90);

	Inorder(root); printf("\n");
	Preorder(root); printf("\n");
	Postorder(root); printf("\n");
	Levelorder(root); printf("\n");
	
	Node * p = SearchNode(root, 4);

	if (p != NULL)
		printf("search: %d\n", p->data);
	
	FreeNode(root);
	return 0;

}
