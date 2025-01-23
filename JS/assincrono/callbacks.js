//SIMULANDO LOGIN USER

const loginUser = (email, password, onSucess, onError) => {
    setTimeout(() => {

        const error = false
        if (error == true) {
            return onError(new Error('error in login'))
        }

        console.log('user logged!');
        onSucess( 
            {
                emailUsuario: email,
                passwordUsuario: password
            }
        ) 
    }, 2000);

    console.log('after setTimeout')
};

const user = loginUser(
    'gustavocostacnn@gmial.com', 
    '123456', 
    (user) => {
        console.log(`user: { email: '${user.emailUsuario}', password: '${user.passwordUsuario}' }`);
    }, 
    (error) => {
        console.log({error});
    }
);
