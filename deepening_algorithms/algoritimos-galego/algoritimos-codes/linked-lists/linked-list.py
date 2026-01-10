class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def add_to_front(self, value):
        """Adiciona um nó no início da lista"""
        new_node = Node(value)
        new_node.next = self.head # Novo nó aponta para a antiga head
        
        if self.head: # Se a lista não estava vazia
            self.head.prev = new_node  #Antiga head aponta para novo nó
        else: # Lista estava vazia
            self.tail = new_node # Tail também é o novo nó

        self.head = new_node# Head agora é o novo n
    
    def add_to_end(self, value):
        """Adiciona um nó no final da lista"""
        new_node = Node(value)
        new_node.prev = self.tail
        
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
    
    def remove_from_front(self):
        """Remove e retorna o primeiro elemento da lista"""
        if not self.head:
            return None
        
        removed_value = self.head.value
        self.head = self.head.next
        
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        
        return removed_value
    
    def remove_from_end(self):  # ← Nome corrigido
        """Remove e retorna o último elemento da lista"""
        if not self.tail:
            return None
        
        removed_value = self.tail.value
        self.tail = self.tail.prev  
        
        if self.tail:
            self.tail.next = None  
        else:
            self.head = None
        
        return removed_value

# Criando lista
dll = DoublyLinkedList()

# Adicionando elementos
dll.add_to_front(3)
dll.add_to_front(2)
dll.add_to_front(1)
dll.add_to_end(4)
dll.add_to_end(5)


# Removendo
print(f"Removido do início: {dll.remove_from_front()}")  # 1
print(f"Removido do final: {dll.remove_from_end()}")     # 5