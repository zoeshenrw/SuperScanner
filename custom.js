function setFormMessage(formElement, type, message){
    const messageElement = formElement.querySelector(".form__message");
    messageElement.textContent = message;
    messageElement.classList.remove("form__message--success", "form__message--error");
    messageElement.classList.add("form__message==${type}");
}

function setInputError(inputElement, message) {
    inputElement.classList.add("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent = message;
}

function clearInputError(inputElement) {
    inputElement.classList.remove("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent = "";
}

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("#login");
    const createAccountForm = document.querySelector("#createAccount");
    const forgotPasswordForm = document.querySelector("#forgotPassword");

    document.querySelector("#linkCreateAccount").addEventListener("click", e =>{
        e.preventDefault();
        loginForm.classList.add("form--hidden");
        createAccountForm.classList.remove("form--hidden");
        forgotPasswordForm.classList.add("form--hidden");
    });

    document.querySelector("#linkLogin").addEventListener("click", e =>{
        e.preventDefault();
        loginForm.classList.remove("form--hidden");
        createAccountForm.classList.add("form--hidden");
        forgotPasswordForm.classList.add("form--hidden");
    });

    document.querySelector("#linkForgotPassword").addEventListener("click", e =>{
        e.preventDefault();
        loginForm.classList.add("form--hidden");
        createAccountForm.classList.add("form--hidden");
        forgotPasswordForm.classList.remove("form--hidden");
    });

    loginForm.addEventListener("submit", e=>{
        e.preventDefault();

        //setFormMessage(loginForm, "success", "You're logged in!");
        setFormMessage(loginForm, "error", "Invalid login combination");
    });

    //does not work yet the statement under if is not showing up
    document.querySelectorAll(".form__input").foreach (inputElement => {
        inputElement.addEventListener("blur", e =>{
            if(e.target.id == "signupPhoneNumber" && e.target.value.length != 10){
                setInputError(inputElement, "Phone Number must only be 10 digits");
            }
        });
        inputElement.addEventListener("input", e =>{
            clearInputError(inputElement);
        });
    });
});