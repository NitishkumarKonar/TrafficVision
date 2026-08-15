const uploadForm =
    document.getElementById("uploadForm");

const videoFile =
    document.getElementById("videoFile");

const uploadStatus =
    document.getElementById("uploadStatus");


uploadForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();

        const file = videoFile.files[0];

        if (!file) {

            uploadStatus.textContent =
                "Please select a video.";

            return;
        }


        const formData =
            new FormData();

        formData.append(
            "file",
            file
        );


        uploadStatus.textContent =
            "Uploading video...";


        try {

            const response =
                await fetch(
                    "/upload",
                    {
                        method: "POST",
                        body: formData
                    }
                );


            const data =
                await response.json();


            if (response.ok) {

                uploadStatus.textContent =
                    "Video uploaded successfully!";

                console.log(data);

                // =========================
                // UPDATE DASHBOARD
                // =========================

                const summary = data.summary;

                document.getElementById("totalVehicles").textContent =
                    summary.total;

                document.getElementById("incomingVehicles").textContent =
                    summary.incoming.total;

                document.getElementById("outgoingVehicles").textContent =
                    summary.outgoing.total;

                document.getElementById("cars").textContent =
                    summary.incoming.car + summary.outgoing.car;

                document.getElementById("motorcycles").textContent =
                    summary.incoming.motorcycle + summary.outgoing.motorcycle;

                document.getElementById("buses").textContent =
                    summary.incoming.bus + summary.outgoing.bus;

                document.getElementById("trucks").textContent =
                    summary.incoming.truck + summary.outgoing.truck;

                // =========================
                // UPDATE PROCESSED VIDEO
                // =========================

                const videoElement =
                    document.getElementById("processedVideo");

                const videoPlaceholder =
                    document.getElementById("videoPlaceholder");

                videoElement.src =
                    "/static/uploads/" + data.output_video;

                videoElement.style.display = "block";

                videoPlaceholder.style.display = "none";

            } else {

                uploadStatus.textContent =
                    "Upload failed.";

            }

        } catch (error) {

            console.error(error);

            uploadStatus.textContent =
                "Something went wrong.";

        }

    }
);