#ifndef LISTS_H
#define LISTS_H

/**
 * struct list_s - singly linked list
 * @n: int
 * @next: pointer to next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif
