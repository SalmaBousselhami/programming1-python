signatures = ['Thomas', 'Invalid_Entry', 'Harriet', 'BadData', 'William']
prepared_petition_signatures = []

print("Processing valid signatures:")
for signature in signatures:
    if signature.startswith('Invalid') or signature.startswith('Bad'):
        print(f"  Skipping invalid: {signature}")
        continue
    
    print(f"  ✓ Valid signature: {signature}")

    pass # you can use `pass` as a placeholder for code you will add later

    prepared_petition_signatures.append(signature)

print("\nPrepared petition signatures:", prepared_petition_signatures)