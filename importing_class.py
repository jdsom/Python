from animal import animal as ani

james = ani("James", "Male", 2, 500)

print(f'Information about pet:')
print(f'\t-Name: {james.name}\n\t' +
      f'-Age: {james.age}\n\t-Gender: {james.gender}\n\t' +
      f'-Weight: {james.weight}lbs')
