// infixtopostfix
#include <iostream>

using namespace std;

struct Stack
{
    int s1[20];
    int top;
    int SZ;
} s;
void push(int value);
int pop();
string infix(string exp);
int precedence(char c);

int main()
{

    s.top = -1;

    string exp;
    cout << "Enter an expression to convert into postfix ";
    cin >> exp;
    cout << infix(exp);
}

void push(int value)
{

    if (s.top == 19)
    {
        cout << "Stack is overflow";
    }
    else
    {
        s.top++;
        s.s1[s.top] = value;
    }
}
int pop()
{
    if (s.top == -1)
    {
        cout << "Stack is underflow";
    }
    else
    {
        int x = s.s1[s.top];
        s.top--;
        return x;
    }
}
int precedence(char c)
{
    if (c == '^')
        return 3;
    else if (c == '*' || c == '/')
        return 2;
    else if (c == '+' || c == '-')
        return 1;

    else
        return -1;
}
string infix(string exp)
{

    int i = 0;
    string postfix = "";
    while (exp[i] != '\0')
    {
        if ((exp[i] >= 'a' && exp[i] <= 'z') || (exp[i] >= 'A' && exp[i] <= 'Z'))
        {
            postfix += exp[i];
            i++;
        }

        else if (exp[i] == '(' || exp[i] == '[' || exp[i] == '{')
        {
            push(exp[i]);
            i++;
        }

        else if (exp[i] == ')')
        {
            while (s.s1[s.top] != '(')
            {
                postfix += pop();
            }
            pop();
            i++;
        }
        else if (exp[i] == ']')
        {
            while (s.s1[s.top] != '[')
            {
                postfix += pop();
            }
            pop();
            i++;
        }
        else if (exp[i] == '}')
        {
            while (s.s1[s.top] != '{')
            {
                postfix += pop();
            }
            pop();
            i++;
        }
        else if (exp[i] == '+' || exp[i] == '-' || exp[i] == '*' || exp[i] == '/')
        {
            if (s.top == -1)
            {
                push(exp[i]);
                i++;
            }

            else if (precedence(exp[i]) > precedence(s.s1[s.top]))
            {
                push(exp[i]);
                i++;
            }
            else
            {
                while (precedence(exp[i]) <= precedence(s.s1[s.top]))
                {
                    postfix += pop();
                }
                push(exp[i]);
                i++;
            }
        }
    }
    while (s.top != -1)
    {

        postfix += pop();
    }

    return postfix;
}
// queue
#include <iostream>

using namespace std;

struct Queue
{

    char q1[5];
    int f;
    int r;

} q;
void insertion(char value);
void deletion();
void display();

int main()
{

    q.f == -1;
    q.r == -1;

    insertion('A');
    insertion('B');
    insertion('C');
    deletion();
    display();
    insertion('F');
    display();
    deletion();
    deletion();
    display();
}
void insertion(char value)
{

    if ((q.f == 0 && q.r == 4) || (q.f == q.r + 1))
    {
        cout << "Overflow";
    }
    else if (q.f == -1 && q.r == -1)
    {
        q.f++;
        q.r++;
    }
    else if (q.f != 0 && q.r == 4)
    {
        q.r = 0;
    }
    else
    {
        q.r++;
        q.q1[q.r] = value;
    }
}
void deletion()
{

    if ((q.r == -1 && q.f == -1) || (q.r < q.f))
    {
        cout << "Underflow";
    }
    else if (q.f == q.r)
    {
        q.r == -1;
        q.f == -1;
    }
    else if (q.f == 4 && q.r > -1)
    {
        q.r == -1;
        q.f == -1;
    }
    else
    {
        q.f++;
    }
}
void display()
{
    int f = q.f;
    int r = q.r;
    if (f == -1)
    {
        cout << "Queue is empty" << endl;
    }
    cout << "Queue elements are :\n";
    if (f <= r)
    {
        while (f <= r)
        {
            cout << q.q1[f] << " ";
            f++;
        }
    }
    else
    {
        while (f <= 4)
        {
            cout << q.q1[f] << " ";
            f++;
        }
        f = 0;
        while (f <= r)
        {
            cout << q.q1[f] << " ";
            f++;
        }
    }

    cout << endl;
}
// bsymbols
#include <iostream>
#include <string>
using namespace std;

struct stack1
{
    char stackChar[20];
    int top;
} s;
// void push(char value);
// int pop();
int n = 20;
void pushChar(char value)
{
    if (s.top == n - 1)
    {
        cout << "Stack overflow" << endl;
        cout << "Empty stack" << endl;
    }
    else
    {
        s.top++;
        s.stackChar[s.top] = value;
    }
}
void popChar()
{
    if (s.top == -1)
    {
        cout << "Stack is underflow" << endl;
        cout << "fill stack" << endl;
    }
    else
    {
        char temp = s.stackChar[s.top];
        s.stackChar[s.top] = 0;
        s.top--;
    }
}
void balancedsym()
{
    string str;
    s.top = -1;

    cout << "The given expression for balancing symbol is:" << endl;
    cin >> str;
    const char *arr = str.c_str();
    for (int i = 0; i < str.length(); i++)
    {
        if (arr[i] == '(' || arr[i] == '{' || arr[i] == '[')
        {
            pushChar(arr[i]);
        }
        else if (arr[i] == ')' || arr[i] == '}' || arr[i] == ']')
        {
            if (s.top == -1)
            {
                cout << "The equation is not balanced" << endl;
                break;
            }
            else
            {
                if (arr[i] == ')' && s.stackChar[s.top] != '(')
                {
                    cout << "the equation is unbalanced" << endl;
                    break;
                }
                else if (arr[i] == '}' && s.stackChar[s.top] != '{')
                {
                    cout << "the equation is unbalanced" << endl;
                    break;
                }
                else if (arr[i] == ']' && s.stackChar[s.top] != '[')
                {
                    cout << "the equation is unbalanced" << endl;
                    break;
                }
                popChar();
            }
        }
    }
    if (s.top == -1)
    {
        cout << "The equation is balanced" << endl;
    }
}
int main()
{
    s.top = -1;
    balancedsym();
}

// bst
#include <iostream>
using namespace std;

struct tree
{
    int info;
    tree *right;
    tree *left;
};

tree *root;

tree *insertion(int val, tree *root);
void displayinorder(tree *root);
void displaypostorder(tree *root);
void displaypreorder(tree *root);

tree *insertion(int val, tree *root)
{
    if (root == NULL)
    {
        tree *p = new tree;
        p->info = val;
        p->left = NULL;
        p->right = NULL;
        root = p;
    }
    else if (root->info == val)
    {
        return root;
    }
    else if (root->info < val)
    {
        root->right = insertion(val, root->right);
    }
    else if (root->info > val)
    {
        root->left = insertion(val, root->left);
    }
    return root;
}

void displayinorder(tree *root)
{
    if (root == NULL)
    {
        return;
    }
    else
    {
        displayinorder(root->left);
        cout << root->info << " ";
        displayinorder(root->right);
    }
}

void displaypostorder(tree *root)
{
    if (root == NULL)
    {
        return;
    }
    else
    {
        displaypostorder(root->left);
        displaypostorder(root->right);
        cout << root->info << " ";
    }
}
void displaypreorder(tree *root)
{
    if (root == NULL)
    {
        return;
    }
    else
    {
        cout << root->info << " ";
        displaypreorder(root->left);
        displaypreorder(root->right);
    }
}

int main()
{
    root = NULL;
    root = insertion(50, root);
    root = insertion(8, root);
    root = insertion(27, root);
    root = insertion(12, root);
    root = insertion(56, root);
    root = insertion(5, root);
    cout << "in order traversal:";
    displayinorder(root);
    cout << endl;
    cout << "post order traversal:";
    displaypostorder(root);
    cout << endl;
    cout << "pre order traversal:";
    displaypreorder(root);

    return 0;
}

// cll
#include <iostream>
#include <cmath>
using namespace std;

struct node
{
    int data;
    node *next;
};

node *list1 = NULL;

void InsertAtStart(int value)
{
    node *q = list1;
    node *p = new node;
    p->data = value;

    if (list1 == NULL)
    {
        list1 = p;
        p->next = list1;
    }
    else
    {
        while (q->next != list1)
        {
            q = q->next;
        }
        p->next = list1;
        list1 = p;
        q->next = list1;
    }
}

void Display()
{
    if (list1 == NULL)
    {
        cout << "list is empty" << endl;
    }
    else
    {
        node *p = list1;
        do
        {
            cout << p->data << " ";
            p = p->next;
        } while (p != list1);
        cout << endl;
    }
}

void InsertAtEnd(int value)
{
    node *q = list1;
    node *p = new node;
    p->data = value;

    if (list1 == NULL)
    {
        list1 = p;
        p->next = list1;
    }
    else
    {
        while (q->next != list1)
        {
            q = q->next;
        }
        q->next = p;
        p->next = list1;
    }
}

void DeleteAtStart()
{
    node *p = list1;
    node *q = list1;
    if (list1 == NULL)
    {
        cout << "list is empty" << endl;
    }
    else
    {
        while (q->next != list1)
        {
            q = q->next;
        }
        list1 = p->next;
        q->next = list1;
        delete (p);
    }
}
void DeleteAtEnd()
{
    node *p = list1;
    node *q = list1;
    if (list1 == NULL)
    {
        cout << "list is empty" << endl;
    }
    else
    {
        while (q->next != list1)
        {
            p = q;
            q = q->next;
        }
        p->next = list1;
        delete (q);
    }
}

int main()
{
    InsertAtStart(2);
    InsertAtStart(8);
    InsertAtStart(5);
    Display();
    InsertAtEnd(3);
    InsertAtEnd(7);
    Display();
    DeleteAtStart();
    Display();
    DeleteAtEnd();
    Display();

    return 0;
}
// dll
#include <iostream>
using namespace std;

struct node
{
    int data;
    node *next;
    node *prev;
};

node *listt = NULL;

void InsertAtStart(int value)
{
    node *p;
    if (listt == NULL)
    {
        p = new node;
        p->data = value;
        p->next = NULL;
        p->prev = NULL;
        listt = p;
    }
    else
    {
        p = new node;
        p->data = value;
        p->next = listt;
        (p->next)->prev = p;
        p->prev = NULL;
        listt = p;
    }
}

void InsertAtEnd(int value)
{
    node *p;
    node *q;
    if (listt == NULL)
    {
        p = new node;
        p->data = value;
        p->next = NULL;
        p->prev = NULL;
        listt = p;
    }
    else
    {
        q = listt;
        while (q->next != NULL)
        {
            q = q->next;
        }
        p = new node;
        p->data = value;
        p->next = NULL;
        q->next = p;
        (q->next)->prev = q;
    }
}

void InsertAtSpecificPosition(int pos, int value)
{
    node *p = listt;
    node *q = NULL;
    int cnt = 1;

    while (p != NULL && cnt < pos)
    {
        q = p;
        p = p->next;
        cnt++;
    }
    if (cnt == pos)
    {
        node *newnode = new node;
        newnode->data = value;

        if (q == NULL)
        {
            newnode->next = listt;
            newnode->prev = NULL;
            if (listt != NULL)
            {
                listt->prev = newnode;
            }
            listt = newnode;
        }
        else
        {
            newnode->next = p;
            newnode->prev = q;
            q->next = newnode;
            if (p != NULL)
            {
                p->prev = newnode;
            }
        }
    }

    else
    {
        cout << "invalid position" << endl;
    }
}

void DeleteAtStart()
{
    node *p;
    if (listt == NULL)
    {
        cout << "list is empty" << endl;
    }
    else
    {
        p = listt;
        listt = p->next;
        (p->next)->prev = NULL;
        delete (p);
    }
}

void DeletAtEnd()
{
    node *p;
    if (listt == NULL)
    {
        cout << "list is empty" << endl;
    }
    else
    {
        p = listt;
        while (p->next != NULL)
        {
            p = p->next;
        }
        (p->prev)->next = NULL;
        delete (p);
    }
}

void Display()
{
    if (listt == NULL)
    {
        cout << "list is empty" << endl;
    }
    else
    {
        node *p = listt;
        while (p != NULL)
        {
            cout << p->data << " ";
            p = p->next;
        }
        cout << endl;
    }
}

void Reverse(node *&listt)
{
    node *p = listt;
    node *temp = NULL;
    while (p != NULL)
    {
        p->prev = temp;
        p->next = p->prev;
        p->next = temp;
        p = p->prev;
    }
    if (temp != NULL)
    {
        listt = temp->prev;
    }
}

int main()
{
    InsertAtStart(4);
    InsertAtStart(7);
    InsertAtStart(6);
    Display();
    InsertAtEnd(3);
    InsertAtEnd(1);
    Display();
    DeleteAtStart();
    Display();
    DeletAtEnd();
    Display();

    InsertAtSpecificPosition(3, 1);
    Display();
    Reverse();
    Display();
    return 0;
}
// llreverseandswap
#include <iostream>

using namespace std;

struct node
{
    int info;
    int num;
    node *next;
};
node *List = NULL;

void insertback(int val);
void displayList();
void swap();
void reverse();

int main()
{
    insertback(1);
    insertback(2);
    insertback(3);
    insertback(4);
    insertback(5);

    while (true)
    {
        cout << "Enter 1 to swap singly Linked List \n";
        cout << "Enter 2 to reverse singly Linked List\n";

        int x;
        cin >> x;
        switch (x)
        {

        case 1:

            displayList();
            swap();
            displayList();
            break;

        case 2:

            displayList();
            reverse();
            displayList();
            break;
        }
    }
}

void swap()
{
    node *q = List;

    if (List == NULL)
    {
        cout << "No node available to swap";
    }
    else
    {
        while (q != NULL)
        {
            if (q->next == NULL)
            {
                return;
            }
            int x = q->info;
            q->info = q->next->info;
            q->next->info = x;
            q = q->next->next;
        }
    }
}

void insertback(int val)
{
    node *p;
    if (List == NULL)
    {
        p = new node;
        p->info = val;
        p->next = NULL;
        List = p;
    }
    else
    {
        node *q;
        q = List;
        while (q->next != NULL)
        {
            q = q->next;
        }
        p = new node;
        p->info = val;
        p->next = NULL;
        q->next = p;
    }
}
void displayList()
{

    if (List == NULL)
        cout << "null";

    else
    {
        node *ptr = List;
        while (ptr != NULL)
        {
            cout << ptr->info << "-->";
            ptr = ptr->next;
        }
        cout << endl;
    }
}
void reverse()
{

    node *prev = NULL;
    node *current = List;
    node *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    List = prev;
}

// linearandbinarysearch
#include <iostream>

using namespace std;

void linearsearch(int key, int arr[]);
void binarysearch(int key, int arr[]);

int main()
{
    int arr[7] = {1, 2, 3, 4, 5, 6, 7};

    binarysearch(5, arr);
}

void linearsearch(int key, int arr[])
{

    for (int i = 0; i <= 6; i++)
    {
        if (key == arr[i])
        {
            cout << "It is Available";
            break;
        }
    }
}
void binarysearch(int key, int arr[])
{
    int flag = 0;

    int high = 7;
    int low = 0;

    while ((low <= high) && (flag == 0))
    {
        int mid = (low + high) / 2;
        if (key == arr[mid])
        {
            flag = 1;
            cout << "Available";
        }
        else if (key < arr[mid])
        {
            high = mid - 1;
        }
        else if (key > arr[mid])
        {
            low = mid + 1;
        }
    }
}
// linearandbinarysearch
#include <iostream>

using namespace std;

void linearsearch(int key, int arr[]);
void binarysearch(int key, int arr[]);

int main()
{
    int arr[7] = {1, 2, 3, 4, 5, 6, 7};

    binarysearch(5, arr);
}

void linearsearch(int key, int arr[])
{

    for (int i = 0; i <= 6; i++)
    {
        if (key == arr[i])
        {
            cout << "It is Available";
            break;
        }
    }
}
void binarysearch(int key, int arr[])
{
    int flag = 0;

    int high = 7;
    int low = 0;

    while ((low <= high) && (flag == 0))
    {
        int mid = (low + high) / 2;
        if (key == arr[mid])
        {
            flag = 1;
            cout << "Available";
        }
        else if (key < arr[mid])
        {
            high = mid - 1;
        }
        else if (key > arr[mid])
        {
            low = mid + 1;
        }
    }
}
// swapdll
#include <iostream>

using namespace std;

struct node
{
    int info;
    node *next;
    node *prev;
};
node *list = NULL;
void insertionEnd(int val);
void displayList();
void swap();

int main()
{

    insertionEnd(1);
    insertionEnd(2);
    insertionEnd(3);
    insertionEnd(4);
    insertionEnd(5);
    displayList();
    swap();
    displayList();
}

void swap()
{
    node *q = list;

    if (list == NULL)
    {
        cout << "No node available to swap";
    }
    else
    {
        while (q != NULL)
        {
            if (q->next == NULL)
            {
                return;
            }
            int x = q->info;
            q->info = q->next->info;
            q->next->info = x;
            q = q->next->next;
        }
    }
}

void insertionEnd(int val)
{
    node *P;
    if (list == NULL)
    {
        P = new node;
        P->info = val;
        P->next = NULL;
        P->prev = NULL;
        list = P;
    }
    else
    {
        node *q = list;
        while (q->next != NULL)
        {
            q = q->next;
        }
        P = new node;
        P->info = val;
        P->next = NULL;
        P->prev = q;
        q->next = P;
    }
}
void displayList()
{

    if (list == NULL)
        cout << "null";

    else
    {
        node *ptr = list;
        while (ptr != NULL)
        {
            cout << ptr->info << "-->";
            ptr = ptr->next;
        }
        cout << endl;
    }
}
#include <iostream>

using namespace std;

struct Node
{
    int info;   // Data value of the node
    Node *next; // Pointer to the next node
};

Node *head1 = NULL; // Initialize the head of the first list to NULL
Node *head2 = NULL; // Initialize the head of the second list to NULL

// Function to insert a value at the end of the first list
void InsertToFirstList(int val)
{
    Node *newNode = new Node; // Create a new node
    newNode->info = val;      // Set its value
    newNode->next = NULL;     // Initialize next to NULL

    if (head1 == NULL)
    {                    // If the first list is empty
        head1 = newNode; // The new node becomes the head
    }
    else
    {
        Node *current = head1; // Start from the head
        while (current->next != NULL)
        { // Traverse to the end
            current = current->next;
        }
        current->next = newNode; // Link the new node
    }
}

// Function to insert a value at the end of the second list
void InsertToSecondList(int val)
{
    Node *newNode = new Node; // Create a new node
    newNode->info = val;      // Set its value
    newNode->next = NULL;     // Initialize next to NULL

    if (head2 == NULL)
    {                    // If the second list is empty
        head2 = newNode; // The new node becomes the head
    }
    else
    {
        Node *current = head2; // Start from the head
        while (current->next != NULL)
        { // Traverse to the end
            current = current->next;
        }
        current->next = newNode; // Link the new node
    }
}

// Function to merge two linked lists into a third linked list
Node *MergeLists(Node *list1, Node *list2)
{
    Node *mergedHead = NULL;      // Head of the merged list
    Node **current = &mergedHead; // Pointer to the last node in merged list

    while (list1 != NULL)
    {                                   // Add all nodes from the first list
        *current = new Node;            // Create a new node
        (*current)->info = list1->info; // Copy value
        (*current)->next = NULL;        // Initialize next to NULL
        current = &((*current)->next);  // Move to the last node in merged list
        list1 = list1->next;            // Move to the next node in list1
    }

    while (list2 != NULL)
    {                                   // Add all nodes from the second list
        *current = new Node;            // Create a new node
        (*current)->info = list2->info; // Copy value
        (*current)->next = NULL;        // Initialize next to NULL
        current = &((*current)->next);  // Move to the last node in merged list
        list2 = list2->next;            // Move to the next node in list2
    }

    return mergedHead; // Return the head of the merged list
}

// Function to display a linked list
void Display(Node *head)
{
    if (head == NULL)
    {
        cout << "Empty" << endl; // If the list is empty
    }
    else
    {
        Node *current = head; // Start from the head
        while (current != NULL)
        {
            cout << current->info << " "; // Print each value
            current = current->next;      // Move to the next node
        }
        cout << endl; // Print a newline after displaying all values
    }
}

// Main function to test the linked list operations
int main()
{
    // Insert values into the first list
    InsertToFirstList(1);
    InsertToFirstList(2);
    InsertToFirstList(3);
    cout << "First List: ";
    Display(head1); // Display the first list

    // Insert values into the second list
    InsertToSecondList(4);
    InsertToSecondList(5);
    InsertToSecondList(6);
    cout << "Second List: ";
    Display(head2); // Display the second list

    // Merge the two lists
    Node *mergedList = MergeLists(head1, head2);
    cout << "Merged List: ";
    Display(mergedList); // Display the merged list

    return 0;
}
#include <iostream>
using namespace std;

struct node
{
    int info;   // Data value of the node
    node *next; // Pointer to the next node
};

node *list = NULL; // Initialize the head of the list to NULL

// Function to insert a value at a specific position
void Insert(int val, int position)
{
    node *P = new node; // Create a new node
    P->info = val;      // Set its value
    P->next = NULL;     // Initialize next to NULL

    if (position == 1)
    {                   // Inserting at the head (position 1)
        P->next = list; // Point new node to current head
        list = P;       // Update head to new node
    }
    else
    {
        node *q = list; // Start from the head
        for (int i = 1; i < position - 1 && q != NULL; i++)
        {
            q = q->next; // Traverse to the position
        }
        if (q != NULL)
        {                      // If position is valid
            P->next = q->next; // Link new node
            q->next = P;       // Insert new node
        }
        else
        {
            cout << "Position out of bounds" << endl; // Invalid position
            delete P;                                 // Clean up
        }
    }
}

// Function to delete a node from a specific position
int Delete(int position)
{
    if (list == NULL)
    {
        cout << "No node to delete" << endl; // If the list is empty
        return -1;                           // Return an invalid value
    }

    if (position == 1)
    {                          // Deleting the head node
        int temp = list->info; // Store the value to return
        node *toDelete = list; // Node to delete
        list = list->next;     // Update head to next node
        delete toDelete;       // Delete the old head
        return temp;           // Return the deleted value
    }
    else
    {
        node *q = list; // Start from the head
        for (int i = 1; i < position - 1 && q != NULL; i++)
        {
            q = q->next; // Traverse to the position
        }
        if (q == NULL || q->next == NULL)
        {
            cout << "Position out of bounds" << endl; // Invalid position
            return -1;                                // Return an invalid value
        }
        int temp = q->next->info; // Store the value of the node to delete
        node *toDelete = q->next; // Node to delete
        q->next = q->next->next;  // Bypass the node to delete
        delete toDelete;          // Delete the node
        return temp;              // Return the deleted value
    }
}

// Function to display the linked list
void Display()
{
    if (list == NULL)
    {
        cout << "Empty" << endl; // If the list is empty
    }
    else
    {
        node *p = list; // Start from the head
        while (p != NULL)
        {
            cout << p->info << " "; // Print each value
            p = p->next;            // Move to the next node
        }
        cout << endl; // Newline after displaying all values
    }
}

// Main function to test the linked list operations
int main()
{
    Insert(4, 1); // Insert 4 at position 1
    Insert(5, 2); // Insert 5 at position 2
    Insert(6, 3); // Insert 6 at position 3
    Display();    // Output: 4 5 6

    Insert(10, 2); // Insert 10 at position 2
    Display();     // Output: 4 10 5 6

    Delete(2); // Delete at position 2
    Display(); // Output: 4 5 6

    Delete(1); // Delete at position 1
    Display(); // Output: 5 6

    Delete(10); // Invalid position
    Display();  // Output: 5 6

    return 0;
}
#include <iostream>
using namespace std;

struct node
{
    int info;
    node *next;
};

node *list = NULL;

void insert(int x)
{
    node *p = new node; // Create a new node
    p->info = x;        // Assign the value
    p->next = NULL;     // Set the next pointer to NULL

    if (list == NULL)
    {             // If the list is empty
        list = p; // Make new node the head
    }
    else
    {
        node *q = list; // Start from the head (using q instead of temp)
        while (q->next != NULL)
        { // Traverse to the end
            q = q->next;
        }
        q->next = p; // Link the new node at the end
    }
}

void deleteEnd()
{ // Deletion function without return value
    if (list == NULL)
    {
        cout << "No node to delete." << endl;
    }
    else
    {
        node *p = list; // Pointer to traverse the list
        node *q;        // Pointer for the previous node
        if (p->next == NULL)
        {                // If there is only one node
            delete p;    // Delete the node
            list = NULL; // Update head to NULL
        }
        else
        {
            while (p->next != NULL)
            {                // Traverse to the second last node
                q = p;       // Keep track of the previous node
                p = p->next; // Move to the next node
            }
            delete p;       // Delete the last node
            q->next = NULL; // Set the next of the second last node to NULL
        }
    }
}

void display()
{
    if (list == NULL)
    {
        cout << "No nodes to display." << endl;
    }
    else
    {
        node *p = list;
        while (p != NULL)
        {
            cout << p->info << " "; // Print each value with a space
            p = p->next;            // Move to the next node
        }
        cout << endl;
    }
}

int main()
{
    insert(4);
    insert(6);
    insert(8);
    display(); // Display the list

    deleteEnd(); // Call the deleteEnd function
    display();   // Display the list after deletion

    return 0;
}
