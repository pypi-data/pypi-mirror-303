import spacy
import re

# Carrega o modelo de linguagem do SpaCy
nlp = spacy.load("pt_core_news_lg")

# Definindo padrões adicionais para CPF, RG, CNPJ, telefone, CEP e endereços
additional_patterns = {
    "CPF": r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b",
    "RG": r"\b\d{1,2}\.\d{3}\.\d{3}-\d{1}\b",
    "CNPJ": r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b",
    "TELEFONE": r"\(\d{2}\) ?9?\d{4}-\d{4}",
    "CEP": r"\b\d{5}-\d{3}\b",
    "ENDERECO": r"\b(Rua|Avenida|Alameda|Travessa|Praça)\s+[A-Za-zÀ-ÿ\s]+,\s*\d+\b"
}

# Lista de entidades que queremos anonimizar do SpaCy
ENTITIES_TO_ANONYMIZE = ["PER", "ORG"]

# Lista de palavras comuns que não devem ser reconhecidas como entidades sensíveis
IGNORED_WORDS = ["olá", "meu nome", "meu cpf", "meu rg", "meu endereço", "empresa", "produto", "bom dia"]

# Lista personalizada de nomes comuns e locais conhecidos que podem não ser reconhecidos corretamente
COMMON_NAMES = ["João", "Maria", "Carlos", "Ana", "Beatriz", "Fernando", "Paulo"]
COMMON_LOCATIONS = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Campinas", "Salvador"]

def anonymize_message_spacy(message):
    # Processa a mensagem com SpaCy para identificar entidades nomeadas
    doc = nlp(message)
    
    # Criar uma lista para armazenar as substituições
    entities_to_anonymize = []

    # Adiciona as entidades detectadas pelo modelo do SpaCy à lista, apenas as relevantes
    for ent in doc.ents:
        if ent.label_ in ENTITIES_TO_ANONYMIZE:
            # Ignorar frases genéricas que não representam dados sensíveis reais
            if ent.text.lower() in IGNORED_WORDS:
                continue
            # Ignorar locais conhecidos que podem ser erroneamente identificados como pessoas
            if ent.text in COMMON_LOCATIONS:
                continue
            entities_to_anonymize.append((ent.start_char, ent.end_char, ent.label_))

    # Adiciona entidades detectadas por padrões adicionais à lista
    for label, pattern in additional_patterns.items():
        for match in re.finditer(pattern, message):
            entities_to_anonymize.append((match.start(), match.end(), label))

    # Adiciona entidades para nomes comuns se encontrados
    for name in COMMON_NAMES:
        for match in re.finditer(rf"\b{name}\b", message, re.IGNORECASE):
            entities_to_anonymize.append((match.start(), match.end(), "PER"))

    # Ordena as entidades pela posição inicial para evitar sobreposição na substituição
    entities_to_anonymize = sorted(entities_to_anonymize, key=lambda x: x[0], reverse=True)

    # Realiza a anonimização das entidades na mensagem original
    anonymized_message = message
    for start, end, label in entities_to_anonymize:
        # Evita substituição duplicada (sobreposição)
        if anonymized_message[start:end].startswith("<"):
            continue
        anonymized_message = anonymized_message[:start] + f"<{label}>" + anonymized_message[end:]

    return anonymized_message
