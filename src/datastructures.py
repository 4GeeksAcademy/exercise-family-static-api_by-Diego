
"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    # 📝 Implementación de método para agregar miembro
    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generate_id()  # ✅ Asignación de ID
        member["last_name"] = self.last_name  # ✅ Asignación de apellido
        self._members.append(member)  # ✅ Agregar miembro a la lista

    # 📝 Implementación de método para eliminar miembro
    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)  # ✅ Eliminación del miembro
                return True
        return False  # ✅ Retorna False si no se encuentra el miembro

    # 📝 Implementación de método para obtener miembro
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member  # ✅ Retorna el miembro encontrado
        return None  # ✅ Retorna None si no se encuentra el miembro

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members  # ✅ Retorna todos los miembros