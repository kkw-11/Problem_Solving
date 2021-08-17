#include <stdio.h>
#include <stdlib.h>

struct _node {
	int data;
	struct _node* prev;
	struct _node* next;
}typedef Node;

Node* AllocNode(int data) {

	Node* n = (Node*)malloc(sizeof(Node));
	n->data = data;
	n->prev = NULL;
	n->next = NULL;

	return n;
}


//void AddList(Node* head, Node** ptail, int data)
//{
//	Node* n = AllocNode(data);
//	(*ptail)->next = n;
//	n->prev = *ptail;
//	*ptail = n;
//}

void AddList(Node* head, Node* tail, int data)
{
	Node* n = AllocNode(data);
	tail->next = n;
	n->prev = tail;
	tail = n;
}

int main(){
	Node* head = NULL;
	Node* tail = NULL;
	Node* n = NULL;
	n = AllocNode(10);
	head = tail = n;

	n = AllocNode(20);
	tail->next = n;
	n->prev = tail;
	tail = n;

	AddList(head,tail, 30);

	for (Node* p = head->next; p->next != NULL; p = p->next)
		printf("%d\n", p->data);

	return 0;
}