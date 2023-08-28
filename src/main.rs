mod socket_utils;

use socket_utils::{UdpClient, Message};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let server_address = "127.0.0.1:8069";

    let udp_client = UdpClient::new()?;
    
    let message = Message {
        content: String::from("Hello from the Rust client!"),
    };

    udp_client.send_message(server_address, message)?;

    Ok(())
}
