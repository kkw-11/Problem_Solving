#include <iostream>
 
using namespace std;
 
struct node {
    int data;
    node *prev, *next;
 
    static node* getNode(int data) {
        node* new_node = new node();
        new_node->data = data;
        new_node->prev = new_node->next = NULL;
        return new_node; //새로운 노드 추가 시 새로운 노드의 전과 다음은 null
    }
};
 
class deque {
    node* front;
    node* rear;
    int size;
 
public:
    deque() {
        front = rear = NULL;
        size = 0;
    }
 
    void insertFront(int data);
    void insertRear(int data);
    void delFront();
    void delRear();
    int getFront();
    int getRear();
    int getSize();
    bool isEmpty();
    void erase();
    void display();
};
 
bool deque::isEmpty() {
    return (front == NULL);
}
 
int deque::getSize() {
    return size;
}
 
void deque::insertFront(int data) {
    node* new_node = node::getNode(data);
    if (new_node == NULL) {
        cout << "deque overflow";
    }
    else {
        cout << "insertFront : " << data;
        if (front == NULL) {
            rear = front = new_node; // 비어있으면 다 같다
        }
        else {
            new_node->next = front; //double이기 때문에 새로운 노드 다음이 프론트
            //앞에 추가되는 거니까
            front->prev = new_node; // front앞이 뉴노드
            front = new_node; // 앞쪽이 뉴노드가 됨
        }
 
        size++; //사이즈 증가
    }
    cout << endl;
}
 
void deque::insertRear(int data) {
    node* new_node = node::getNode(data);
    if (new_node == NULL) {
        cout << "deque overflow"; //new_node가 null이면 꽉 찼다는 것
    }
    else {
        cout << "insertRear : " << data;
        if (rear == NULL) {
            front = rear = new_node; //아무것도 없으니 다 같다
        }
        else {
            new_node->prev = rear;
            rear->next = new_node;
            rear = new_node;
        }
        size++;
    }
    cout << endl;
}
 
void deque::delFront() {
    if (isEmpty()) {
        cout << "deque underflow";
    }
    else { //큐에 원소하나라도 있다면
        cout << "delFront : " << front->data;
        node* temp = front; //임시로 프론트 저장
        front = front->next; // 프론트가 삭제되기 때문에 프론트는
        //기존 프론트 다음이 된다
 
        if (front == NULL) {
            rear = NULL; //새로운 프론트가 없으면 rear도 NULL
        }
        else {
            front->prev = NULL; //있으면 front 전 노드는 없으므로 NULL
        }
        free(temp);
        size--; //삭제했으므로 크기 줄어듦
    }
    cout << endl;
}
 
void deque::delRear() {
    if (isEmpty()) {
        cout << "deque underflow";
    }
    else {
        cout << "delRear : " << rear->data;
 
        node* temp = rear; //뒤에서 삭제하니까 rear로 초기화
        rear = rear->prev; //새로운 레어는 기존 레어 전
        
        if (rear == NULL) {
            front = NULL; //끝이 없으면 프론트도 없다(왜냐면 새로운 레어는 기존 레어 전이니까)
        }
        else {
            rear->next = NULL; //레어가 null이 아니면 레어다음은 null 끝이기 때문
        }
        free(temp);
        size--; //삭제했기 때문에 size 감소
    }
    cout << endl;
}
 
int deque::getFront() {
    if (isEmpty()) {
        return -1;
    }
    else {
        return front->data;
    }
}
 
int deque::getRear() {
    if (isEmpty()) {
        return -1;
    }
    else {
        return rear->data;
    }
}
 
void deque::erase() { //전체삭제
    rear = NULL;
    node* temp = front;
    while (temp != NULL) {
        free(temp);
        temp = temp->next;
    }
    size = 0;
}
 
void deque::display() {
    node* temp = front;
    cout << "deque element : ";
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}
 
int main() {
    deque dq;
 
    dq.insertFront(-1);
    dq.insertFront(-2);
    dq.insertFront(-3);
 
    dq.display();
 
    dq.insertRear(1);
    dq.insertRear(2);
    dq.insertRear(3);
 
    dq.display();
 
    cout << "current front : " << dq.getFront()
        << " current rear : " << dq.getRear() << endl;
 
    dq.delFront();
    dq.delRear();
 
    dq.display();
 
    cout << "current front : " << dq.getFront()
        << " current rear : " << dq.getRear() << endl;
 
    return 0;
}
