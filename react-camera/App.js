import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity, Slider, Vibration } from 'react-native';
import {Constants, Camera, FileSystem, Permissions } from 'expo';

export default class CameraExample extends React.Component {
        state = {
                        hasCameraPermission: null,
                        type: Camera.Constants.Type.back,
                };

        async componentWillMount() {
                const { status } = await Permissions.askAsync(Permissions.CAMERA);
                this.setState({ hasCameraPermission: status === 'granted' });
        }

        takePicture = async function() {
                if (this.camera) {
                        Vibration.vibrate();
                        this.camera.takePictureAsync().then(data => {
                                FileSystem.moveAsync({
                                        from: data.uri,
                                        to: `${FileSystem.documentDirectory}photos/posterphoto.jpg`,
                                }).then(() => {
                                        Vibration.vibrate();
                                });
                        });
                }
        };
        render() {
                const { hasCameraPermission } = this.state;
                if (hasCameraPermission === null) {
                        return <View />;
                } else if (hasCameraPermission === false) {
                        return <Text>No access to camera</Text>;
                } else {
                        return (
                                <View style={{ flex: 1 }}>
                                <Camera
                                 style={{ flex: 1 }}
                                 type={this.state.type}
                                 ratio={'16:9'}>
                                 <View
                                 style={{
                                         flex: 1,
                                         backgroundColor: 'transparent',
                                         flexDirection: 'row',
                                 }}>
                                 <TouchableOpacity
                                 style= {[styles.flipButton,
                                         styles.picButton,
                                         { flex: 0.3, alignSelf: 'flex-end' }]}
                                           onPress={this.takePicture.bind(this)}>
                                           <Text style={styles.flipText}> SNAP </Text>
                                </TouchableOpacity>
                                </View>
                                </Camera>
                                </View>
                        );
                }
        }
}

const styles = StyleSheet.create({
        flipButton: {
                flex: 0.3,
                height: 40,
                marginHorizontal: 2,
                marginBottom: 10,
                marginTop: 20,
                borderRadius: 8,
                borderColor: 'white',
                borderWidth: 1,
                padding: 5,
                alignItems: 'center',
                justifyContent: 'center',
        },
        flipText: {
                color: 'white',
                fontSize: 15,
        },
        picButton: {
                backgroundColor: 'darkseagreen',
        }
});
