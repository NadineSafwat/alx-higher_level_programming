#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to list
 * Return: 1 if it has a cycle and 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *p2;
	listint_t *pre;

	p2 = list;
	pre = list;
	while (list && p2 && p2->next)
	{
		list = list->next;
		p2 = p2->next->next;
		if (list == p2)
		{
			list = pre;
			pre =  p2;
			while (1)
			{
				p2 = pre;
				while (p2->next != list && p2->next != pre)
				{
					p2 = p2->next;
				}
				if (p2->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
