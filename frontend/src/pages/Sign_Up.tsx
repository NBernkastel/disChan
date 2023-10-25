import axios from 'axios';
import React, { useState } from 'react';
import { Button, Container, Row, Col, Form } from 'react-bootstrap';

const RegistrationForm: React.FC = () => {
  const [userData, setUserData] = useState({
    username: '',
    email: '',
    password: ''
  });

  const registerUser = async () => {
    try {
      const response = await axios.post('http://localhost:8084/auth/reg', userData);
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
        <h2 className="text-center mb-4">Sign Up</h2>
        <Form>
          <Form.Group controlId="username">
            <Form.Label>Username</Form.Label>
            <Form.Control type="text" name="username" onChange={handleInputChange} value={userData.username} />
          </Form.Group>
          <Form.Group controlId="email">
            <Form.Label>Email</Form.Label>
            <Form.Control type="email" name="email" onChange={handleInputChange} value={userData.email} />
          </Form.Group>
          <Form.Group controlId="password">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" name="password" onChange={handleInputChange} value={userData.password} />
          </Form.Group>
          <Button variant="primary" onClick={registerUser}className="mt-3">Register</Button>
        </Form>
      </div>
    </div>
  );
}

export default RegistrationForm;