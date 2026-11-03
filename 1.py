import asyncio
import os

import streamlit as st

# Sahifa sozlamalari
st.set_page_config(
    page_title="Dostoevsky — Native Audio Reader",
    page_icon="📚",
    layout="wide",
)

# Native AI ovozlar ro'yxati (Buyuk Britaniya va AQSH)
VOICES = {
    "Ryan (UK Erkak - Tabiiy Hikoyachi)": "en-GB-RyanNeural",
    "Sonia (UK Ayol - Aniq va Ravon)": "en-GB-SoniaNeural",
    "Guy (US Erkak - Amerika Talaffuzi)": "en-US-GuyNeural",
    "Jenny (US Ayol - Amerika Yangiliklar Uslubi)": "en-US-JennyNeural",
}

# Maqolaning to'liq matni
FULL_ARTICLE_TEXT = """The Most Dangerous Writer Who Ever Lived

What if the most dangerous writer in history was not someone who persuaded people to hate, but someone who made them question everything they believed about themselves?

Imagine a young man sitting alone in a cramped room in nineteenth-century St Petersburg. He has committed a murder, convinced himself that he had a philosophical justification for it, and now finds that he cannot escape his own thoughts. Nobody needs to arrest him for his punishment to begin. His mind has already become a prison.

This is the world of Fyodor Dostoevsky, the Russian novelist who spent much of his literary life exploring the uncomfortable territory between good and evil, freedom and responsibility, faith and despair. His books have unsettled readers for more than a century because they do something that many writers avoid: they refuse to let us feel entirely innocent.

Calling Dostoevsky the most dangerous writer who ever lived is, of course, a provocative description. He was not dangerous because he commanded armies or organised political movements. His power was different. He exposed the contradictions people conceal beneath their respectable identities, and he asked questions that become particularly disturbing when readers recognise themselves in the answers.

The Execution That Changed His Life

Dostoevsky was born in Moscow in 1821, the son of a doctor, and initially trained as a military engineer in St Petersburg. His first novel, Poor Folk, published in 1846, attracted favourable attention and introduced a writer unusually attentive to the emotional lives of people living in poverty. But his literary career was interrupted by politics.

In 1849, he was arrested for participating in discussions associated with the Petrashevsky Circle, a group of intellectuals who debated social and political ideas, including the abolition of serfdom. The authorities treated the group as a threat. Dostoevsky and other prisoners were sentenced to death, but the execution was staged: after they had been brought before a firing squad and prepared for death, a message arrived commuting their sentences.

The experience was designed to terrify. Dostoevsky was then sent to a Siberian prison camp, where he spent four years before being required to serve in the military. The years of imprisonment and exile changed his understanding of human suffering, punishment and the limits of abstract political theories. His later book The House of the Dead, drawing on prison life, would offer readers an unusually intimate view of the people society preferred to forget.

There is a temptation to treat this experience as the single explanation for everything he later wrote. That would be too simple. But the prison years gave him direct contact with people whose lives could not easily be reduced to categories such as criminal, innocent, respectable or corrupt. In his fiction, even characters who commit terrible acts are given histories, fears and competing impulses.

The Murderer Who Cannot Escape Himself

In Crime and Punishment, published in 1866, Dostoevsky creates one of literature's most unsettling experiments in moral psychology. Rodion Raskolnikov, an impoverished former student, believes that certain exceptional individuals have the right to transgress ordinary moral rules if they can serve a greater purpose. He tests this theory by murdering a pawnbroker.

What follows is not a conventional detective story in which the central pleasure comes from discovering who committed the crime. The reader knows almost immediately. The real mystery is whether Raskolnikov can live with what he has done, and whether his intellectual justification can survive the pressure of guilt, fear and human connection.

Dostoevsky's insight is that people do not always behave according to the principles they claim to believe. Raskolnikov has constructed an elaborate argument to place himself above ordinary morality, yet his body and mind resist the identity he has invented. He becomes feverish, suspicious and increasingly isolated.

The novel is dangerous in a particular sense: it makes the reader experience the seduction of a bad idea before revealing its human cost. Rather than simply telling us that arrogance can lead to cruelty, Dostoevsky allows us to follow the reasoning that makes cruelty appear defensible.

Inside the Underground Mind

Three years before Crime and Punishment, Dostoevsky published Notes from Underground, a short, unsettling work narrated by a bitter and isolated man who seems determined to contradict himself. He is intelligent enough to recognise his own weaknesses, but not willing to change them. He longs for respect while resenting those from whom he wants it.

The Underground Man is disturbing because he does not behave like the rational individual imagined by many political and philosophical theories. He sometimes chooses what harms him simply to demonstrate that he is free to choose. He would rather make a destructive decision of his own than behave like a predictable machine.

This is one of Dostoevsky's most enduring challenges to the idea that human beings can be understood entirely through logic, incentives or material interests. People are capable of acting against their apparent advantage, not because they have no reason, but because pride, resentment and the desire for independence can become more important than comfort.

Modern readers may recognise aspects of this character in the endless cycle of online arguments, self-sabotage and resentment that can consume people who are desperate to be acknowledged but unwilling to accept vulnerability. Dostoevsky did not predict social media, of course. He understood something older: the human capacity to turn one's own suffering into an identity.

The Most Uncomfortable Question

Dostoevsky's final great novel, The Brothers Karamazov, published in 1880, brings many of his lifelong concerns together through a family divided by resentment, faith, intellectual rebellion and moral responsibility. At its centre is a question that refuses to remain comfortably theoretical: if people are free to choose their actions, what responsibility do they carry for the suffering that follows?

One of the novel's most famous sections, "The Grand Inquisitor", imagines Christ returning to a society governed by religious authority. Instead of welcoming him, the Grand Inquisitor arrests him. The argument is that human beings do not really want the burden of freedom; they want security, certainty and someone powerful enough to make decisions for them.

It is a disturbing challenge because it questions not only political authority but also the motives behind obedience. People may surrender freedom willingly when uncertainty becomes unbearable. They may prefer a comforting explanation to a difficult truth, even when that explanation requires them to give up part of their independence.

Dostoevsky's novels repeatedly return to this tension. His characters want to be good, but they are capable of cruelty. They desire freedom, yet sometimes fear the responsibility it brings. They search for meaning while being tempted by ideas that promise simple answers to complicated human problems.

His own political and religious convictions were complex, and modern readers do not need to agree with them to recognise the force of his questions.

Why He Still Makes Readers Uncomfortable

Dostoevsky died in St Petersburg in 1881, shortly after completing The Brothers Karamazov. His influence continued far beyond Russian literature. Writers and philosophers, including Albert Camus and Jean-Paul Sartre, engaged with the problems of freedom, absurdity and moral responsibility that his fiction had explored.

What makes his writing feel so contemporary is not that he predicted every crisis of modern society. It is that he understood how easily people can become prisoners of their own explanations. A person can justify almost anything if they spend long enough constructing a theory that places them on the right side of it.

That is why Dostoevsky may deserve the provocative title of the most dangerous writer who ever lived. He does not simply expose the cruelty of villains or the corruption of institutions. He turns the investigation towards the reader, making it harder to believe that evil belongs exclusively to other people.

His books do not offer the comfort of a clean division between good people and bad ones. They leave us with something more demanding: the possibility that understanding human darkness begins by admitting that it is not entirely unfamiliar."""

# Lug'at ma'lumotlari
VOCABULARY = [
    (
        "1. Transgress",
        "to break a rule, moral boundary or accepted standard.",
        "He was willing to transgress social expectations to pursue his ambitions.",
    ),
    (
        "2. Commute",
        "to reduce or change a punishment, especially a legal sentence.",
        "The president decided to commute the prisoner's sentence.",
    ),
    (
        "3. Seduction",
        "the process of attracting someone towards an idea, action or belief.",
        "The seduction of quick success can lead people to make reckless decisions.",
    ),
    (
        "4. Resentment",
        "persistent bitterness caused by feeling unfairly treated.",
        "Years of resentment damaged their relationship.",
    ),
    (
        "5. Contradiction",
        "a situation in which two ideas or statements cannot both be true.",
        "There is a contradiction between his promises and his actions.",
    ),
    (
        "6. Vulnerability",
        "the state of being emotionally or physically exposed to harm.",
        "Admitting that you are struggling can be a sign of vulnerability, not weakness.",
    ),
    (
        "7. Arrogance",
        "an exaggerated sense of one's own importance or abilities.",
        "His arrogance prevented him from listening to useful advice.",
    ),
    (
        "8. Isolation",
        "the state of being separated from other people or society.",
        "Working from home for long periods can sometimes lead to social isolation.",
    ),
    (
        "9. Moral responsibility",
        "the obligation to accept accountability for one's actions and their consequences.",
        "Leaders have a moral responsibility to consider how their decisions affect ordinary people.",
    ),
]

# Savollar ro'yxati
QUESTIONS = [
    (
        "1. Do you believe that people are fundamentally good, or are they"
        " capable of both good and evil depending on their circumstances?"
    ),
    (
        "2. Can intelligence sometimes make people better at justifying their"
        " mistakes rather than recognising them?"
    ),
    (
        "3. Why do some people prefer security and certainty over personal"
        " freedom and responsibility?"
    ),
    (
        "4. Do you agree that understanding a criminal's psychological"
        " motivations can help us understand crime without excusing it?"
    ),
    (
        "5. Which is more dangerous: a person who knows they are doing"
        " something wrong, or someone who genuinely believes their harmful"
        " actions are justified?"
    ),
]


async def generate_speech_file(
    text: str, voice: str, rate: str, output_path: str
):
    """Edge-TTS orqali audio yaratuvchi asinxron funksiya"""
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    await communicate.save(output_path)


# Yon panel (Sidebar)
with st.sidebar:
    st.header("🎙️ Audio Sozlamalari")
    chosen_label = st.selectbox("Native Diktor Tanlang:", list(VOICES.keys()))
    voice_code = VOICES[chosen_label]

    rate_percent = st.slider(
        "O'qish tezligi (%):",
        min_value=-25,
        max_value=25,
        value=0,
        step=5,
        format="%d%%",
    )
    rate_str = f"{rate_percent:+d}%"

    st.markdown("---")
    st.markdown("### 📌 Qo'shimcha Manbalar")
    st.caption("1. Fyodor Dostoevsky — Biography and major works")
    st.caption("2. Treccani: Dostoevsky's life and literary career")
    st.caption("3. SparkNotes: Crime and Punishment")
    st.caption("4. SparkNotes: The Brothers Karamazov")

# Bosh sahifa
st.title("📖 Fyodor Dostoevsky: The Most Dangerous Writer Who Ever Lived")
st.markdown(
    "Matnni o'qishingiz hamda uni yuqori sifatli **native ingliz diktori** ovozida tinglashingiz mumkin."
)

tab1, tab2, tab3 = st.tabs(
    ["📄 To'liq Maqola", "🧠 Advanced Vocabulary", "❓ Discussion Questions"]
)

with tab1:
    st.subheader("Maqola Matni")
    text_content = st.text_area(
        "Matnni xohlaganingizcha tahrirlashingiz mumkin:",
        value=FULL_ARTICLE_TEXT,
        height=400,
    )

    col_btn, _ = st.columns([2, 5])
    with col_btn:
        start_tts = st.button(
            "🔊 Matnni Ovozga Aylantirish",
            type="primary",
            use_container_width=True,
        )

    audio_file_name = "dostoevsky_article.mp3"

    if start_tts:
        if not text_content.strip():
            st.warning("Iltimos, avval matn kiriting!")
        else:
            with st.spinner("Native diktor matnni ovozlashtirmoqda..."):
                try:
                    asyncio.run(
                        generate_speech_file(
                            text=text_content,
                            voice=voice_code,
                            rate=rate_str,
                            output_path=audio_file_name,
                        )
                    )
                    st.success("Audio tayyor bo'ldi!")

                    with open(audio_file_name, "rb") as f:
                        audio_data = f.read()

                    st.audio(audio_data, format="audio/mp3")
                    st.download_button(
                        label="📥 MP3 faylni yuklab olish",
                        data=audio_data,
                        file_name="dostoevsky_native_audio.mp3",
                        mime="audio/mp3",
                    )
                except Exception as err:
                    st.error(f"Xatolik yuz berdi: {err}")

with tab2:
    st.subheader("📚 Advanced Vocabulary")
    for word, meaning, example in VOCABULARY:
        with st.expander(f"🔹 {word}"):
            st.write(f"**Meaning:** {meaning}")
            st.write(f"**Example:** *{example}*")

with tab3:
    st.subheader("💬 Muhokama Savollari")
    for q in QUESTIONS:
        st.info(q)
