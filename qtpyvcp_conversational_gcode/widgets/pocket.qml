import QtQuick 2.7
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.3


Rectangle {
    id: rectangle1
    visible: true
    width: 420
    clip: false
    transformOrigin: Item.Center
    height: 200
    border.color: "#00000000"

    Rectangle{
        transformOrigin: Item.Center
        id: stock
        visible: true
        anchors.fill: parent
        color: "white"
        border.color: "#00000000"

        Canvas {
            id: canvas
            width: 420
            height: 200
            contextType: qsTr("")

            property real safe_z: 0.0
            property real part_z_zero: 0.0
            property real step_down: 0.0
            property real finishZ: 40.0

            property int lineWidth: 2
            property int nSize: 10
            property real radius: 0
            property bool fill: true
            property bool stroke: false
            property real px: width/2
            property real py: height/2 + 20
            property real alpha: 1.0

            signal propertyChanged
            x: 0
            y: 0
            antialiasing: true

            onFinishZChanged: requestPaint();
            onRadiusChanged: requestPaint();
            onLineWidthChanged: requestPaint();
            onNSizeChanged: requestPaint();
            onFillChanged: requestPaint();
            onStrokeChanged:requestPaint();
            onImageLoaded : requestPaint();
            onPaint: draw_pocket();

            function draw_pocket() {
                console.log("DRAW")
                var ctx = canvas.getContext("2d");
                ctx.reset();
                ctx.beginPath();

                ctx.moveTo(10, 10);
                ctx.lineTo(100, 10);
                ctx.lineTo(100, canvas.finishZ);
                ctx.lineTo(300, canvas.finishZ);
                ctx.lineTo(300, 10);
                ctx.lineTo(410, 10);
                ctx.lineTo(410, 120);
                ctx.lineTo(10, 120);

                ctx.closePath();


                var pattern = ctx.createPattern("#554444", Qt.BDiagPattern);

                ctx.globalAlpha = canvas.alpha;

                ctx.strokeStyle = "black";
                ctx.fillStyle = pattern;
                ctx.lineWidth = canvas.lineWidth;


                ctx.stroke();
                ctx.fill();

                ctx.clip();

                ctx.save();
            }
        }

        border.width: 1
        anchors.verticalCenterOffset: 1
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }

    Component.onCompleted: {

    }

    function set_safe_z(safe_z) {
        console.log("SAFE Z" + safe_z)
        canvas.safeZ = safe_z
    }

    function set_part_z_zero(part_z_zero) {
        console.log("Z ZERO" + part_z_zero)
        canvas.partZZero = part_z_zero
    }

    function set_step_down(step_down) {
        console.log("STEP DOWN" + step_down)
        canvas.stepDown = step_down
    }

    function set_finish_z(finish_z) {
        console.log("FINISH Z" + finish_z)
        canvas.finishZ = finish_z
    }

    Connections {
        target: handler

        onSetSafeZSig: {
            set_safe_z(safe_z)
        }

        onSetPartZeroSig: {
            set_part_z_zero(part_z_zero)
        }

        onSetStepDownSig: {
            set_step_down(step_down)
        }

        onSetFinishZSig: {
            set_finish_z(finish_z)
        }
    }

}








/*##^## Designer {
    D{i:2;anchors_height:40;anchors_y:0}D{i:1;anchors_y:148}
}
 ##^##*/
