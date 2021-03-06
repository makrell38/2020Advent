//Working for part 1
#include <string>
#include <iostream>


using namespace std;

int size = 0;


class cup{
    public:
        int val;
        cup* before;
        cup* after;
};

void print(cup* head, int dest)
{
    cup* temp = head;
    cout<<"Cups:  ";
    if(temp->val == dest){
            cout<<"("<<temp->val<<") ";
        }
        else
            cout<<temp->val<<" ";
        temp = temp->after;
    while(temp != head){
        if(temp->val == dest){
            cout<<"("<<temp->val<<") ";
        }
        else
            cout<<temp->val<<" ";
        temp = temp->after;
    }
    cout<<endl;
}

void insertCup(int num, cup* head){
    cup* insert = new cup();
    insert->val = num;
    cup* temp = head;
    while(temp->after != head){
        temp = temp->after;
    }
    temp->after = insert;
    insert->before = temp;
    insert->after = head;
    head->before = insert;
    size++;
}

int main()
{
    string final = "";
    cup* head = new cup();
    head->val = 3;
    head->before = head;
    head->after = head;
    size++;
    insertCup(8, head);
    insertCup(9, head);
    insertCup(5, head);
    insertCup(4, head);
    insertCup(7, head);
    insertCup(6, head);
    insertCup(1, head);
    insertCup(2, head);

    cup** pickUp = new cup*[3];
    for(int i = 0; i < 3; i++){
        pickUp[i] = new cup[1];
    }
    cup* dest = new cup();
    cup* temp = head;
    cup* next = head;
    int loc = 0;
    int k, find, j;
    for(int n = 0; n < 100; n++){
        cout<<"-- move "<<n+1<<" --"<<endl;
        
        temp = head;
        next = head;
        for(int i = 0; i < loc; i++){
            next = next->after;
        }
        print(head,next->val);
        k = 0;
        while(k != 1){
            if(temp->val == next->val){
                
                pickUp[0] = temp->after;
                pickUp[1] = pickUp[0]->after;
                pickUp[2] = pickUp[1]->after;
                temp->after = pickUp[2]->after;
                pickUp[2]->after->before = temp;
                if(pickUp[0] == head || pickUp[1] == head || pickUp[2] == head)
                    head = temp->after;
                k = 1;
            }
            else
                temp = temp->after;
        }
        cout<<"pick up:  "<<pickUp[0]->val<<", "<<pickUp[1]->val<<", "<<pickUp[2]->val<<endl;

        
        find = 0;
        j = next->val;
        temp = head;
        j = j - 1;
        if(j < 1)
            j = 9;
  
        while(j == pickUp[0]->val || j == pickUp[1]->val || j == pickUp[2]->val){
            j = j - 1;
            if(j < 1)
                j = 9;
        }
        cout<<"destination:  "<<j<<endl;
        for(int i = 0; i < 6; i++){
            if(temp->val == j){
                dest = temp;
            }
            temp = temp->after;
        } 


        pickUp[2]->after = dest->after;
        pickUp[2]->after->before = pickUp[2];
        dest->after = pickUp[0];
        pickUp[0]->before = dest;

        temp = head;
        
        while (temp->val != next->val){
            temp = temp->after;
        }
        for(int i = 0; i < loc; i++){
            temp = temp->before;

        }
        head = temp;
 
        cout<<endl<<endl;

        loc=(loc+1)%9;
    }

    next = head;
    for(int i = 0; i < loc; i++){
        next = next->after;
    }
    cout<<"-- final --"<<endl;
    print(head, next->val);

    temp = head;
    while(temp->val != 1){
        temp = temp->after;
    }
    for(int i = 0; i < size-1; i++){
        temp = temp->after;
        final += std::to_string(temp->val);
    }
    cout<<final<<endl;

    return 0;
}