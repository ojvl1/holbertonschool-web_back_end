import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      const profilePic = values[0].body;
      const name = values[1].firstName;
      const { lastName } = values[1];
      console.log(`${[profilePic]} ${name} ${lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
