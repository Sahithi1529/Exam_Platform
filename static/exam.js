const questions = [
    {
        question: "1. Which statement is true about Java?",
        answers: [
            {text:"Java is a sequence-dependent programming language", correct: false},
            {text: "Java is a code dependent programming language", correct: false},
            {text: "Java is a platform-dependent programming language", correct: false},
            {text: "Java is a platform-independent programming language", correct: true},
        ]
    },
    {
        question: "2. Which component is used to compile, debug and execute the java programs?",
        answers: [
            {text:"JRE", correct: false},
            {text: "JIT", correct: false},
            {text: "JDK", correct: true},
            {text: "JVM", correct: false},
        ]
    },
    {
        question: "3. Which one of the following is not a Java feature?",
        answers: [
            {text:"Object-oriented", correct: false},
            {text: "Use of pointers", correct: true},
            {text: "Portable", correct: false},
            {text: " Dynamic and Extensible", correct: false},
        ]
    },
    {
        question: "4. Which of these cannot be used for a variable name in Java?",
        answers: [
            {text:"identifier & keyword", correct: false},
            {text: "identifier", correct: false},
            {text: "keyword", correct: true},
            {text: "none of the mentioned", correct: false},
        ]
    },
    {
        question: "5. What is the extension of java code files?",
        answers: [
            {text:".js", correct: false},
            {text: ".txt", correct: false},
            {text: ".class", correct: false},
            {text: ".java", correct: true},
        ]
    },
    {
        question: "6. Which environment variable is used to set the java path?",
        answers: [
            {text:"MAVEN_Path", correct: false},
            {text: "JavaPATH", correct: false},
            {text: "JAVA", correct: false},
            {text: "JAVA_HOME", correct: true},
        ]
    },
    {
        question: "6.Which of the following is not an OOPS concept in Java?",
        answers: [
            {text:"Polymorphism", correct: false},
            {text: "Inheritance", correct: false},
            {text: "Compilation", correct: true},
            {text: "Encapsulation", correct: false},
        ]
    },
    {
        question: "7.What is not the use of “this” keyword in Java?",
        answers: [
            {text:"Referring to the instance variable when a local variable has the same name", correct: false},
            {text: "Passing itself to the method of the same class", correct: true},
            {text: "Passing itself to another method", correct: false},
            {text: " Calling another constructor in constructor chaining", correct: false},
        ]
    },
      
];

const questionElement = document.getElementById("question");
const answerButtons = document.getElementById("answer-buttons");
const nextButton = document.getElementById("next-btn");

let currentQuestionIndex = 0;
let score = 0;

function startQuiz(){
    currentQuestionIndex = 0;
    score = 0;
    nextButton.innerHTML = "Next";
    showQuestion();
}

function showQuestion(){
    resetState();
    let currentQuestion = questions[currentQuestionIndex];
    let questionNo = currentQuestionIndex + 1;
    questionElement.innerHTML = questionNo + ". " + currentQuestion.question;

    currentQuestion.answers.forEach(answer => {
        const button = document.createElement("button");
        button.innerHTML = answer.text;
        button.classList.add("btn");
        answerButtons.appendChild(button);
        if(answer.correct){
            button.dataset.correct = answer.correct;
        }
        button.addEventListener("click", selectAnswer);
    });
}

function resetState(){
    nextButton.style.display = "none";
    while(answerButtons.firstChild){
        answerButtons.removeChild(answerButtons.firstChild);
    }
}

function selectAnswer(e){
    const selectedBtn = e.target;
    const isCorrect = selectedBtn.dataset.correct === "true";
    if(isCorrect){
        selectedBtn.classList.add("correct");
        score++;
    }else{
        selectedBtn.classList.add("incorrect");
    }
    Array.from(answerButtons.children).forEach(button => {
        if(button.dataset.correct === "true"){
            button.classList.add("correct");
        }
        button.disabled = true;
    });
    nextButton.style.display = "block";
}

function handleNextButton(){
    currentQuestionIndex++;
    if(currentQuestionIndex < questions.length){
        showQuestion();
    }else{
        showScore();
    }
}

function showScore(){
    resetState();
    questionElement.innerHTML = `You scored ${score} out of ${questions.length}!`;
    nextButton.innerHTML = "Play Again";
    nextButton.style.display = "block";
}

nextButton.addEventListener("click", () => {
    if(currentQuestionIndex < questions.length){
        handleNextButton();
    }else{
        startQuiz();
    }
});

startQuiz();

