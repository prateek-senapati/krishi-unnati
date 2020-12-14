import React from 'react'; 
import { StyleSheet,  View, Button, Image, TouchableOpacity } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { NavigationContainer } from '@react-navigation/native';
import Profile from './Profile';
import {
  createDrawerNavigator,
  DrawerContentScrollView,
  DrawerItemList,
  DrawerItem,
} from '@react-navigation/drawer';
import {
  useTheme,
  Avatar,
  Title,
  Caption,
  Paragraph,
  Drawer,
  Text,
  TouchableRipple,
  Switch,
} from 'react-native-paper';

export default function Header() {

  return (
    <View style={styles.whole} >
      <View style={styles.header} >
 
         <Text style={styles.titless}>KRISHI UNNATI</Text>    
      </View>


     <Image style={{ marginTop:0,height:610,width:500,opacity:0.5 }}source={require('../assets/iconKU.jpeg')} />
    
       <TouchableOpacity style={styles.design} onPress={Profile} >
         <Text style={styles.insidetext}>Click here to upload/scan photo</Text>
       </TouchableOpacity>
    </View>
    
  );
}


const styles = StyleSheet.create({
    
  drawerContent: {
    flex: 1,
  },
  userInfoSection: {
    paddingLeft: 20,
  },
  title: {
    marginTop: 20,
    fontWeight: 'bold',
  },
  caption: {
    fontSize: 14,
    lineHeight: 14,
  },
  row: {
    marginTop: 20,
    flexDirection: 'row',
    alignItems: 'center',
  },
  section: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 15,
  },
  paragraph: {
    fontWeight: 'bold',
    marginRight: 3,
  },
  drawerSection: {
    marginTop: 15,
  },
  preference: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 12,
    paddingHorizontal: 16,
  },
    whole:{
       padding:0,
       margin:0
    },
    header: {
     height: 70, 
     paddingTop: 21,
     backgroundColor: '#00BD56',
     flexDirection: 'row',
    },
    titless:{
        fontWeight:'bold',
        color:'#fff',
        textAlign: 'center',
        fontSize: 25,
        marginTop:0,
        marginLeft: 130,
    },
    tl:{
        marginLeft: 15,
        color:'#fff',
        paddingTop :0,
        
    },
    btn:{
        paddingTop: 200
    },
    btntext:{
      color:'black',
    },
    design:{
      position:'absolute',
      color:'red',
      marginTop:520,
      paddingLeft:120,
      paddingRight:100,
    },
    insidetext:{
        backgroundColor:'red',
        margin:0,
        padding:10,
        textAlign:'center',
        color:'white',
        borderRadius:50,
        justifyContent:'center'
    }
  });