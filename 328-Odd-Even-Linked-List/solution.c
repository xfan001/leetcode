
typedef struct ListNode Node;

struct ListNode* oddEvenList(struct ListNode* head) {
    if (!head) {
        return head;
    }
    
    Node *Pj=head, *Po=head->next;
    Node *Headj = head;
    Node *Heado = head->next;
    while (Po && Po->next) {
        Pj->next = Po->next;
        Pj = Pj->next;
        Po->next = Pj->next;
        Po = Po->next;
    }
    Pj->next = Heado;
    
    return Headj;
}