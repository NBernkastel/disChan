import axios from 'axios';
import React, { useState } from 'react';
import { Button, Form } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
// @ts-ignore
import Cookies from 'js-cookie';

const LoginForm: React.FC = () => {
  const [userData, setUserData] = useState({
    login: '',
    password: ''
  });

  const navigate = useNavigate(); // Используем useNavigate для навигации

  const loginUser = async () => {
    try {
      const response = await axios.post('http://localhost:8000/auth/login', userData);
      const { access_token } = response.data;

      // Сохранение токена в cookie
      Cookies.set('access_token', access_token, { expires: 7, secure: true, sameSite: 'Strict' });

      console.log('Login successful');

      // Перенаправление на главную страницу
      navigate('/main');
    } catch (error) {
      console.error('Login error:', error);
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
            Don't have an account? <Link to="/signup">Sign Up</Link>
          </div>
        </Form>
      </div>
    </div>
  );
}

export default LoginForm;
