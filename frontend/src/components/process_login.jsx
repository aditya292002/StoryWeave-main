import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { setCookie, checkValidToken } from '../assets/scripts/login_info'

function ProcessLogin() {
  const navigate = useNavigate();

  // If the token is present and not expired
  if (checkValidToken()) {
    return (
      <>
      code for the story
      </>
    )
  }

  else {
    const handleSubmit = async (event) => {
      event.preventDefault();

      const email = event.target.elements.email.value;
      const password = event.target.elements.password.value;

      try {
        // // check if username exists
        const responseCheck = await axios.post('http://localhost:8000/check', { email, password });

        //  if the user is a new user then create account
        if (responseCheck.data.details === 'New User') {
          const responseCreateAccount = await axios.post('http://localhost:8000/users', { email, password });
          if (responseCreateAccount.status === 201) {
            console.log("User Successfully created");
          } else {
            console.log("Try again");
            event.target.reset();
            return; // Stop execution if user creation fails
          }
        }

        // User exists or user sucessfully created
        console.log("Going for login")
        const responseLogin = await axios.post('http://localhost:8000/login', { email, password });
        console.log(responseLogin);

        setCookie('access_token', responseLogin.data.access_token, 24*60); // Change this value accordingly
        console.log(responseLogin.data.access_token);

        navigate('/Room');
      } catch (error) {
        console.error('Error:', error);
      }
    };

    return (
      <div className="container col-xl-10 col-xxl-8 px-4 py-5" style={{ background: "#f8edeb" }}>
          <div className="row align-items-center g-lg-5 py-5">
              <div className="col-lg-7 text-center text-lg-start">
                  <h1 className="display-4 fw-bold lh-1 text-body-emphasis mb-3">Welcome to the Quiz Web App</h1>
                  <p className="col-lg-10 fs-4">
                      Get ready to test your knowledge with our interactive quiz platform. Answer questions, earn points, and compete with others to reach the top of the leaderboard.
                  </p>
              </div>
              <div className="col-md-10 mx-auto col-lg-5">
                  <form className="p-4 p-md-5 border rounded-3 bg-body-tertiary" onSubmit={handleSubmit}>
                      <div className="form-floating mb-3">
                          <input type="email" className="form-control" id="floatingInput" name="email" placeholder="name@example.com" />
                          <label htmlFor="floatingInput">Email address</label>
                      </div>
                      <div className="form-floating mb-3">
                          <input type="password" className="form-control" id="floatingPassword" name="password" placeholder="Password" />
                          <label htmlFor="floatingPassword">Password</label>
                      </div>
                      <div className="checkbox mb-3">
                          <label>
                              {/* <input type="checkbox" value="remember-me" /> Remember me */}
                          </label>
                      </div>
                      <button className="w-100 btn btn-lg btn-primary" type="submit">
                          Sign up
                      </button>
                      <hr className="my-4" />
                      <small className="text-body-secondary">By clicking Sign up, you agree to the terms of use.</small>
                  </form>
              </div>
          </div>
      </div>
    );
  }
};

export default ProcessLogin;
