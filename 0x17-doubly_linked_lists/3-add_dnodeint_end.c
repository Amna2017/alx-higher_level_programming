#include "lists.h"

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
dlistint_t *TempNode = NULL; /* Points to the new node */
dlistint_t *NodeListCounterOne = NULL;  /* Traverse to the needed node */
TempNode = (dlistint_t *)malloc(sizeof(dlistint_t));
if(NULL != TempNode)
{
	TempNode->Noden = n;
	TempNode->RightNodeLink = NULL;
	NodeListCounterOne = List;
	while(NULL != NodeListCounterOne->RightNodeLink)
	{
		NodeListCounterOne = NodeListCounterOne->dlistint_t.next;
	}
	TempNode->LeftNodeLink = NodeListCounterOne;
	NodeListCounterOne->dlistint_t.next = TempNode;
	return (TempNode);
}
else{
	return ;
}
}
