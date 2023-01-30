
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int info;
    struct Node * next;
};
typedef struct Node ListElement;
typedef ListElement * List;

List GetData() {
    List l = NULL;

    int n;
    printf("Insert number [-1: END]: ");
    scanf("%d", &n);

    if (n != -1) {
        ListElement * new = malloc(sizeof(ListElement));
        new -> info = n;
        new -> next = NULL;
        l = new;

        printf("Insert number: ");
        scanf("%d", &n);
        List last = l;
        while (n != -1) {
            new = malloc(sizeof(ListElement));
            new -> info = n;
            new -> next = NULL;
            last -> next = new;
            last = new;

            printf("Insert number: ");
            scanf("%d", &n);
        }
    }

    return l;
}

void PrintList_index(List l, int n) {
    if (l == NULL) {
        return;
    }
    printf("List [%d] :  %d\n", n, l -> info);
    PrintList_index(l -> next, n+1);
}
void PrintList(List l) {
    PrintList_index(l, 0);
}

int ListCount(List l) {
    int c = 0;

    while (l != NULL) {
        c++;
        l = l -> next;
    }

    return c;
}

List List_GetLast(List l) {
    if (l == NULL) return l;
    while ((l -> next) != NULL) {
        l = l -> next;
    }
    return l;
}

List ListCopy(List l) {
    if (l == NULL) {
        return NULL;
    }
    List l2 = malloc(sizeof(ListElement));
    List l2_last = malloc(sizeof(ListElement));
    l2 -> info = l -> info;
    l2_last = l2;

    l = l -> next;
    while (l != NULL) {
        List new = malloc(sizeof(ListElement));
        new -> info = l -> info;
        new -> next = NULL;
        l2_last -> next = new;
        l2_last = new;
        l = l -> next;
    }
    
    return l2;
}

List ListConcat_J(List a, List b, int J) {
    if (a == NULL) return b;
    if (b == NULL) return a;

    List A;
    List B;
    if (J <= 0) {
        A = b;
        B = a;
    } else {
        A = a;
        B = b;
    }

    List last = List_GetLast(A);
    last -> next = B;
    return A;
}

void main() {
    printf("\nGetData [1]\n");
    List data = GetData();

    printf("\nPrintList\n");
    PrintList(data);

    printf("\nListCount\n");
    printf("Count: %d\n", ListCount(data));

    printf("\nGetData [2]\n");
    List data2 = GetData();

    printf("\nListConcat_J\n");
    int J;
    printf("Insert J [>0 A|B; <=0 B|A] :  ");
    scanf("%d", &J);
    PrintList(ListConcat_J(ListCopy(data), ListCopy(data2), J));


}