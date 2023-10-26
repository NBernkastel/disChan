import axios from 'axios';
import React, { useState } from 'react';
import { Button, Form } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const LoginForm: React.FC = () => {
  const [userData, setUserData] = useState({
    login: '',
    password: ''
  });

  const loginUser = async () => {
    try {
      const response = await axios.post('http://localhost:8084/auth/login', userData);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setUserData((prevUserData) => ({
      ...prevUserData,
      [name]: value
    }));
  }

  return (
    <div className="bg-dark text-white d-flex align-items-center justify-content-center" style={{ minHeight: '70vh' }}>
      <div>
        <h2 className="text-center mb-4">Sign In</h2>
        <Form>
          <Form.Group controlId="login">
            <Form.Label>Login</Form.Label>
            <Form.Control type="text" name="login" onChange={handleInputChange} value={userData.login} />
          </Form.Group>
          <Form.Group controlId="password">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" name="password" onChange={handleInputChange} value={userData.password} />
          </Form.Group>
          <Button variant="primary" onClick={loginUser} className="mt-3">Login</Button>
          <div className="mt-2 text-center">
            Don't have an account? <Link to="/Sign Up">Sign Up</Link>
          </div>
        </Form>
      </div>
    </div>
  );
}

export default LoginForm;