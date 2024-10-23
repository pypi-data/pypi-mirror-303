class NLPUtils:
    def __init__(self):
        print(
            """
    p1: Tokenization, stemming, lemmatization, stop words removal, Sentiment Analysis
    p2: Text generation using GPT-2
    p3: Tokenization using NLTK, regex, and BERT
    p4: N-gram generation and probability calculation
    p5: N-gram probability calculation with Laplace, Lidstone, and Good-Turing smoothing
    p6: Part-of-speech tagging using NLTK
    p7: Chunking using fixed-size, sliding window, and punctuation-based methods
    p8: CFG parsing using NLTK
    
    """
        )

    def p1(self):
        code = """
        Tokenization, stemming, lemmatization, stop words removal, Sentiment Analysis:
        import nltk
        from nltk.tokenize import word_tokenize
        from nltk.corpus import stopwords
        from nltk.stem import PorterStemmer, WordNetLemmatizer
        from nltk.classify import NaiveBayesClassifier
        from nltk.sentiment import SentimentAnalyzer
        from nltk.sentiment.util import extract_unigram_feats

        text = "Ishaan likes NLP"

        tokens = word_tokenize(text)

        # Stopwords removal
        stop_words = set(stopwords.words('english'))
        tokens_without_stopwords = [word for word in tokens if word.lower() not in stop_words]

        # Stemming
        porter = PorterStemmer()
        stemmed_tokens = [porter.stem(word) for word in tokens_without_stopwords]
        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens_without_stopwords]

        print("Original tokens:")
        print(tokens)
        print("Tokens after stopwords removal:")
        print(tokens_without_stopwords)
        print("Stemmed tokens:")
        print(stemmed_tokens)
        print("Lemmatized tokens:")
        print(lemmatized_tokens)

        labeled_data = [({'word': 'amazing'}, 'positive'), ({'word': 'terrible'}, 'negative')]
        # Initialize sentiment analyzer
        sentim_analyzer = SentimentAnalyzer()
        # Extract features from tokens
        training_set = sentim_analyzer.apply_features(labeled_data, extract_unigram_feats)
        # Train NaiveBayesClassifier
        trainer = NaiveBayesClassifier.train
        classifier = sentim_analyzer.train(trainer, training_set)

        # Example sentence for sentiment analysis
        sentence = "This movie was amazing!"

        # Preprocess the sentence
        tokens = word_tokenize(sentence)
        tokens_without_stopwords = [word for word in tokens if word.lower() not in stop_words]
        stemmed_tokens = [porter.stem(word.lower()) for word in tokens_without_stopwords]
        features = sentim_analyzer.extract_features({word: True for word in stemmed_tokens})

        # Predict sentiment
        print("Predicted sentiment:")
        print(classifier.classify(features))
        """
        print(code)

    def p2(self):
        code = """
    !pip install transformers torch

    # Import libraries
    from transformers import GPT2LMHeadModel, GPT2Tokenizer
    import torch

    model_name = 'gpt2'  # You can also use 'gpt2-medium', 'gpt2-large', etc. for larger models
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    prompt = "Once upon a time, in a magical kingdom"

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = model.to(device)

    # Tokenize input prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

    # Parameters for text generation
    max_length = 100  # Maximum length of the generated text in tokens
    temperature = 0.7  # Controls the randomness of predictions; lower temperature means more deterministic
    top_k = 50  # Controls diversity via top-k sampling
    top_p = 0.95  # Controls diversity via nucleus sampling
    num_return_sequences = 1  # Number of different sequences to generate
    repetition_penalty=1.2

    # Generate text based on input prompt
    outputs = model.generate(
        input_ids,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        repetition_penalty=repetition_penalty,
        top_p=top_p,
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id  # Stop generating at the end of a sentence
    )

    # Decode and print the generated text
    for output in outputs:
        generated_text = tokenizer.decode(output, skip_special_tokens=True)
        print(generated_text)
        """
        print(code)


    def p3(self):
        code = """
        pip install nltk
        from nltk.tokenize import word_tokenize, sent_tokenize
        import re
        from transformers import BertTokenizer
        import os

        # NLTK tokenization examples
        text = "This is a sample sentence."
        tokens = word_tokenize(text)
        print("Word Tokenization:", tokens)

        text = 'Hello, world! How are you?'
        sentences = sent_tokenize(text)
        for sentence in sentences:
            print("Sentence Tokenization:", word_tokenize(sentence))

        # Regex tokenization example
        def regex_tokenizer(text, pattern=r'\\w+'):
            return re.findall(pattern, text)

        text = "Tokenize-this-text-with-regex"
        tokens = regex_tokenizer(text)
        print("Regex Tokenization:", tokens)

        # Transformers BERT tokenizer example
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

        # Define the file path
        file_path = 'example.txt'

        # Check if file exists, if not, create and populate it with sample text
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write("This is some example text to demonstrate tokenization using BERT.")

        # Now read the file and tokenize it using BERT tokenizer
        with open(file_path, 'r') as file:
            text = file.read()

        tokens = tokenizer.tokenize(text)
        print("BERT Tokenization:", tokens)
        """
        print(code)


    def p4(self):
        code = """
        import nltk
        from nltk.util import ngrams
        from nltk import FreqDist
        from nltk.tokenize import word_tokenize
        from collections import defaultdict

        nltk.download('punkt')

        def preprocess(text):
            return word_tokenize(text.lower())

        def generate_ngrams(tokens, n):
            return list(ngrams(tokens, n))

        def calculate_probabilities(ngrams_list, n):
            freq_dist = FreqDist(ngrams_list)

            if n == 1:
                total_unigrams = sum(freq_dist.values())
                probabilities = {word: freq / total_unigrams for word, freq in freq_dist.items()}
            else:
                prefix_freq_dist = FreqDist(ngram[:-1] for ngram in ngrams_list)
                probabilities = defaultdict(lambda: defaultdict(float))

                for ngram in freq_dist:
                    prefix = ngram[:-1]
                    suffix = ngram[-1]
                    if prefix_freq_dist[prefix] > 0:
                        probabilities[prefix][suffix] = freq_dist[ngram] / prefix_freq_dist[prefix]

            return probabilities

        def print_probabilities(probabilities):
            if isinstance(next(iter(probabilities.values())), float):
                for word, prob in probabilities.items():
                    print(f'Word: {word}, Probability: {prob:.4f}')
            else:
                for prefix, suffixes in probabilities.items():
                    print(f'Prefix: {prefix}')
                    for suffix, prob in suffixes.items():
                        print(f'  Suffix: {suffix}, Probability: {prob:.4f}')

        text = input()

        tokens = preprocess(text)

        unigrams = generate_ngrams(tokens, 1)
        unigram_probs = calculate_probabilities(unigrams, 1)
        print("Unigram Probabilities:")
        print_probabilities(unigram_probs)

        bigrams = generate_ngrams(tokens, 2)
        bigram_probs = calculate_probabilities(bigrams, 2)
        print("Bigram Probabilities:")
        print_probabilities(bigram_probs)

        trigrams = generate_ngrams(tokens, 3)
        trigram_probs = calculate_probabilities(trigrams, 3)
        print("Trigram Probabilities:")
        print_probabilities(trigram_probs)
        """
        print(code)


    def p5(self):
        code = """
        import nltk
        from nltk.util import ngrams
        from nltk import FreqDist
        from nltk.tokenize import word_tokenize
        from collections import defaultdict

        nltk.download('punkt')

        def preprocess(text):
            return word_tokenize(text.lower())

        def generate_ngrams(tokens, n):
            return list(ngrams(tokens, n))

        def laplace_smoothing(ngrams_list, n):
            freq_dist = FreqDist(ngrams_list)
            if n == 1:
                total_unigrams = sum(freq_dist.values())
                vocabulary_size = len(freq_dist)
                probabilities = {word: (freq + 1) / (total_unigrams + vocabulary_size) for word, freq in freq_dist.items()}
            else:
                prefix_freq_dist = FreqDist(ngram[:-1] for ngram in ngrams_list)
                vocabulary_size = len(set(ngram[-1] for ngram in ngrams_list))
                probabilities = defaultdict(lambda: defaultdict(float))

                for ngram in freq_dist:
                    prefix = ngram[:-1]
                    suffix = ngram[-1]
                    probabilities[prefix][suffix] = (freq_dist[ngram] + 1) / (prefix_freq_dist[prefix] + vocabulary_size)

            return probabilities

        def lidstone_smoothing(ngrams_list, n, alpha=0.5):
            freq_dist = FreqDist(ngrams_list)
            if n == 1:
                total_unigrams = sum(freq_dist.values())
                vocabulary_size = len(freq_dist)
                probabilities = {word: (freq + alpha) / (total_unigrams + alpha * vocabulary_size) for word, freq in freq_dist.items()}
            else:
                prefix_freq_dist = FreqDist(ngram[:-1] for ngram in ngrams_list)
                vocabulary_size = len(set(ngram[-1] for ngram in ngrams_list))
                probabilities = defaultdict(lambda: defaultdict(float))

                for ngram in freq_dist:
                    prefix = ngram[:-1]
                    suffix = ngram[-1]
                    probabilities[prefix][suffix] = (freq_dist[ngram] + alpha) / (prefix_freq_dist[prefix] + alpha * vocabulary_size)

            return probabilities

        def good_turing_smoothing(ngrams_list, n):
            freq_dist = FreqDist(ngrams_list)
            count_freq = FreqDist(freq_dist.values())

            total_ngrams = len(ngrams_list)
            probabilities = defaultdict(lambda: defaultdict(float))

            for count, freq in count_freq.items():
                if count == 0:
                    continue
                next_count = count_freq.get(count + 1, 0)
                prob = (count + 1) * next_count / (total_ngrams * count)

                for ngram in freq_dist:
                    prefix = ngram[:-1]
                    suffix = ngram[-1]
                    if freq_dist[ngram] == count:
                        probabilities[prefix][suffix] = prob

            vocab_size = len(set(ngram[-1] for ngram in ngrams_list))
            unseen_prob = count_freq.get(1, 0) / total_ngrams
            for prefix in probabilities:
                for suffix in set(ngram[-1] for ngram in ngrams_list):
                    if suffix not in probabilities[prefix]:
                        probabilities[prefix][suffix] = unseen_prob

            return probabilities

        def print_probabilities(probabilities):
            if isinstance(next(iter(probabilities.values())), float):
                for word, prob in probabilities.items():
                    print(f'Word: {word}, Probability: {prob:.4f}')
            else:
                for prefix, suffixes in probabilities.items():
                    print(f'Prefix: {prefix}')
                    for suffix, prob in suffixes.items():
                        print(f'  Suffix: {suffix}, Probability: {prob:.4f}')

        text = "The quick brown fox jumps over the lazy dog. The fox is very quick."

        tokens = preprocess(text)
        for n in range(1, 4):
            ngrams_list = generate_ngrams(tokens, n)

            print(f"Unigram Probabilities ({'Laplace' if n == 1 else 'Higher-order'}):")
            unigram_probs = laplace_smoothing(ngrams_list, n) if n == 1 else laplace_smoothing(ngrams_list, n)
            print_probabilities(unigram_probs)

            print(f"Bigram Probabilities ({'Lidstone' if n == 2 else 'Higher-order'}):")
            bigram_probs = lidstone_smoothing(ngrams_list, n) if n == 2 else lidstone_smoothing(ngrams_list, n)
            print_probabilities(bigram_probs)

            print(f"Trigram Probabilities ({'Good-Turing' if n == 3 else 'Higher-order'}):")
            trigram_probs = good_turing_smoothing(ngrams_list, n) if n == 3 else good_turing_smoothing(ngrams_list, n)
            print_probabilities(trigram_probs)

        """
        print(code)


    def p6(self):
        code = """
        import nltk
        from nltk.tokenize import sent_tokenize, word_tokenize
        from nltk import pos_tag

        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')

        pos_descriptions = {
            'NN': 'Noun',
            'JJ': 'Adjective',
            'VB': 'Verb',
            'RB': 'Adverb',
            'DT': 'Determiner',
            'IN': 'Preposition',
            'PRP': 'Pronoun',
            'MD': 'Modal',
            'CC': 'Conjunction',
            'TO': 'to'
        }

        def describe_pos_tag(tag):
            tag_prefix = tag[:2]
            return pos_descriptions.get(tag_prefix, 'Other')

        paragraph = '''
        Incorporating the emotional context into recommendation systems can lead to more empathetic, satisfying, and serendipitous user experiences. If an engine can recognize the user's real-time emotional state and adapt its suggestions accordingly, it can potentially keep the user more positively engaged!
        '''

        sentences = sent_tokenize(paragraph)
        print("Tokenized sentences:", sentences)

        for sentence in sentences:
            print(f"Processing sentence: {sentence}")

            words = word_tokenize(sentence)

            tagged_words = pos_tag(words)

            for word, tag in tagged_words:
                print(f"{word}: {tag} ({describe_pos_tag(tag)})")
        """
        print(code)

    def p7(self):
        code = """
    import nltk
    from nltk.tokenize import word_tokenize

    nltk.download('punkt')

    text = "The quick brown fox jumps over the lazy dog. The weather is pleasant today, and I feel excited to go for a walk."

    words = word_tokenize(text)

    def fixed_size_chunking(words, chunk_size):
        chunks = [words[i:i+chunk_size] for i in range(0, len(words), chunk_size)]
        return chunks

    chunk_size = 5
    fixed_chunks = fixed_size_chunking(words, chunk_size)

    for i, chunk in enumerate(fixed_chunks):
        print(f"Chunk {i+1}: {chunk}")

    def sliding_window_chunking(words, window_size, step_size):
        chunks = [words[i:i+window_size] for i in range(0, len(words), step_size)]
        return chunks

    window_size = 5
    step_size = 3
    sliding_chunks = sliding_window_chunking(words, window_size, step_size)

    for i, chunk in enumerate(sliding_chunks):
        print(f"Chunk {i+1}: {chunk}")

    from nltk.tokenize import sent_tokenize

    sentences = sent_tokenize(text)

    for i, sentence in enumerate(sentences):
        print(f"Chunk {i+1}: {sentence}")

    import re

    def punctuation_based_chunking(text):
        chunks = re.split(r'(?<=[.!?])\s+', text)
        return chunks

    punctuation_chunks = punctuation_based_chunking(text)

    for i, chunk in enumerate(punctuation_chunks):
        print(f"Chunk {i+1}: {chunk}")

        """
        print(code)

    def p8(self):
        code = """
        # Install NLTK (if you don't have it installed already)
        !pip install nltk

        # Import necessary NLTK components
        import nltk
        from nltk import CFG, pos_tag
        from nltk.tokenize import word_tokenize, sent_tokenize
        from nltk.parse import ChartParser
        from nltk.chunk import ne_chunk
        import sys

        # Step 1: Download necessary NLTK resources
        nltk.download('punkt')  # Tokenizer
        nltk.download('averaged_perceptron_tagger')  # POS Tagging
        nltk.download('maxent_ne_chunker')  # Named Entity Recognition
        nltk.download('words')  # NER requires the list of words

        # Step 2: Define a simple CFG grammar for sentence parsing
        cfg_grammar = CFG.fromstring("""
        S -> NP VP
        NP -> Det N | Det N PP | 'I' | 'Barack' 'Obama' | 'the' 'United' 'States'
        VP -> V NP | VP PP
        PP -> P NP
        Det -> 'the' | 'a'
        N -> 'man' | 'park' | 'dog' | 'telescope' | 'President'
        V -> 'saw' | 'walked' | 'served'
        P -> 'in' | 'with' | 'as' | 'of'
        """)

        # Example sentence for CFG parsing
        sentence = "Barack Obama served as the President of the United States".split()

        # Step 3: Use ChartParser (more efficient than RecursiveDescentParser)
        parser = ChartParser(cfg_grammar)

        # Parse the sentence using the ChartParser
        print("Parsing result with ChartParser:")
        for tree in parser.parse(sentence):
            print(tree)

        # Step 4: Named Entity Recognition (NER)

        # Example text with named entities
        text = "Barack Obama was born in Hawaii and served as the President of the United States."

        # Tokenize the sentence into words and POS tag them
        words = word_tokenize(text)
        pos_tags = pos_tag(words)

        # Perform Named Entity Recognition
        named_entities_tree = ne_chunk(pos_tags)

        # Display the named entity tree
        print("Named Entity Recognition (NER) result:")
        print(named_entities_tree)

        # Step 5: Extract and classify named entities

        # Function to classify and extract named entities from the NER tree
        def extract_named_entities(ne_tree):
            entities = []
            for subtree in ne_tree:
                if isinstance(subtree, nltk.Tree):
                    entity = " ".join([word for word, pos in subtree.leaves()])
                    entity_type = subtree.label()  # The entity type (e.g., PERSON, GPE, ORGANIZATION)
                    entities.append((entity, entity_type))
            return entities

        # Extract named entities from the tree
        named_entities = extract_named_entities(named_entities_tree)

        # Display the named entities and their types
        print("Extracted Named Entities:")
        for entity, entity_type in named_entities:
            print(f"Entity: {entity}, Type: {entity_type}")

        # Step 6: Parsing multiple sentences in a larger text using CFG and NER

        # Additional text for parsing and NER
        large_text = '''
        Barack Obama was born in Hawaii. He served as the President of the United States.
        Apple Inc. is a technology company headquartered in Cupertino, California.
        '''

        # Tokenize the large text into sentences
        sentences = sent_tokenize(large_text)

        # Process each sentence with CFG parsing and NER
        for sent in sentences:
            print(f"Processing sentence: {sent}")

            # Tokenize and POS tag the sentence
            words = word_tokenize(sent)
            pos_tags = pos_tag(words)

            # Perform CFG parsing with ChartParser
            print("Parsing result with ChartParser:")
            try:
                for tree in parser.parse(words):
                    print(tree)
            except ValueError as e:
                print(f"Parsing Error: {e}")

            # Perform Named Entity Recognition (NER)
            print("Named Entity Recognition result:")
            named_entities_tree = ne_chunk(pos_tags)
            print(named_entities_tree)

            # Extract named entities
            named_entities = extract_named_entities(named_entities_tree)

            # Display extracted entities
            print("Extracted Named Entities:")
            for entity, entity_type in named_entities:
                print(f"Entity: {entity}, Type: {entity_type}")
        """
        print(code)
