const attendees = [
  { id: 1, x: 12.4, y: 7.8 },
  { id: 2, x: 15.9, y: 9.3 },
  { id: 3, x: 9.1, y: 6.5 }
];

function updatePositions() {
  console.log("📍 [Attendee Tracking] Updating positions...");
  attendees.forEach((a) => {
    a.x += Math.random() * 2 - 1;
    a.y += Math.random() * 2 - 1;
    console.log(`Attendee ${a.id}: (${a.x.toFixed(2)}, ${a.y.toFixed(2)})`);
  });
}

setInterval(updatePositions, 2000);
