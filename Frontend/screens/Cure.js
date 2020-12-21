import React from 'react';
import { View, Text, StyleSheet, Button, Alert, Image } from 'react-native';

class Cure extends React.Component {

    constructor(props) {
        super(props);
    
        this.state = {
            cure:props.navigation.state.params.cure,
        }
        console.log(props.navigation.state.params)
      }
    

    render() {

        return (

            <View style={styles.container}>
                <Text style={styles.buttonText}><Text style={{fontWeight:'bold'}}>Details </Text> -- {this.state.cure}</Text>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center'
    },
    buttonText:{
        alignItems: 'center',
        justifyContent: 'center',
    }
})

export default Cure