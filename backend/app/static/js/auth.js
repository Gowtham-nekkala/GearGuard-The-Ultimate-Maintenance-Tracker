// LOGIN LOGIC
const loginForm = document.getElementById("loginForm");

if (loginForm) {
  loginForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const email = loginEmail.value.trim();
    const password = loginPassword.value.trim();

    if (!email || !password) {
      loginError.innerText = "All fields are required";
      return;
    }

    // Backend integration point
    alert("Login request submitted");
  });
}

// SIGNUP LOGIC
const signupForm = document.getElementById("signupForm");

if (signupForm) {
  signupForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const pwd = signupPassword.value;
    const confirmPwd = signupConfirmPassword.value;

    const strongPassword =
      pwd.length >= 8 &&
      /[A-Z]/.test(pwd) &&
      /[a-z]/.test(pwd) &&
      /[0-9]/.test(pwd) &&
      /[^A-Za-z0-9]/.test(pwd);

    if (!strongPassword) {
      signupError.innerText =
        "Password must be 8+ chars with uppercase, lowercase, number & special char";
      return;
    }

    if (pwd !== confirmPwd) {
      signupError.innerText = "Passwords do not match";
      return;
    }

    // Backend integration point
    alert("Signup request submitted");
  });
}
