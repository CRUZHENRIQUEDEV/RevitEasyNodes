#Esse script retorna filtrado todos os inputs que são true

# Listas de valores booleanos
boolean_lists = IN[0]
# Função para encontrar os índices onde o valor é True
def indices_of_true(boolean_list):
    true_indices = [i for i, value in enumerate(boolean_list) if value == True]
    return true_indices

# Loop através das listas e encontre os índices onde o valor é True
results = []
for boolean_values in boolean_lists:
    result = indices_of_true(boolean_values)
    results.append(result)

# Resultados
OUT = results
