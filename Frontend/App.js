import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import Login from './screens/Login';
import Signup from './screens/Signup';
import Profile from './screens/Profile';
import Header from './screens/Header';

const navigator = createStackNavigator({
  
  Login: Login,
  Signup: Signup,
  // Header: Header,
  Profile: Profile
}, {
  initialRouteName: 'Login',
  defaultNavigationOptions: {                                             
    title: 'Krishi Unnati'
  }
});

export default createAppContainer(navigator);




 